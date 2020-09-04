#!/usr/bin/env python
""" Source code for scoring districting plans. This includes population,
contiguity and the full score which combines them """

from math import exp as e
from statistics import pstdev

from utils import distr_count
from utils import distr_pop
from utils import contig_distr


def score_plan(plan, const):
    """ Accepts a districting plan in the form of a networkx graph and scores
    it using two sub-scores: population balance and district contiguity. The
    score function takes the form of an energy function: e^-x. A parameterised
    constant is used to appropriately scale the results of the sub-scores """

    # Get population score parameter
    pop_param = score_pop(plan)

    # Get contiguity score parameter
    contig_param = score_contig(plan)

    # Energy function with constant to adjust 'strength' of scoring
    score = e(-const * pop_param * contig_param)

    return score


def score_pop(plan):
    """ Score a supplied plan for its population balance. That is, check the
    population variance of each district from the ideal average. Returns a
    variance value """

    # Retrieve the number of districts in the given plan and create empty list
    # for population values from each district
    num_distrs = distr_count(plan)
    distr_pops = []

    for i in range(1, num_distrs + 1):
        # Tabulate population of each district and append to list
        distr_pops.append(distr_pop(i, plan))

    # pstdev is the standard library standard deviation function for an
    # iterable input
    std_dev = pstdev(distr_pops)
    var = std_dev ** 2

    return var


def score_contig(plan):
    """ Scores a supplied plan based on the number of contiguous districts
    present. If all are contiguous, returns 1; elsec returns 10^6 """

    num_distrs = distr_count(plan)

    # Build up a list of results for the contiguity test
    contig_list = []
    for i in range(1, num_distrs + 1):
        contig_list.append(contig_distr(i, plan))

    # Count the number of disconnected districts and set score value
    if all(contig_list):
        score = 1
    else:
        score = 1000000

    return score
