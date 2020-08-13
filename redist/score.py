#!/usr/bin/env python
""" Source code for scoring districting plans """

from utils import distr_count
from utils import distr_pop
from utils import contig_distr
from math import exp as e
from statistics import pstdev


def score_plan(plan, const):
    """ Accepts a districting plan in the form of a networkx graph and scores
    it for apportionment equality. The score function takes the form of an
    energy function using the standard deviation of the population of each
    district """

    # Get population score parameter
    pop_param = score_pop(plan)

    # Get contiguity score parameter
    contig_param = score_contig(plan)

    # Energy function with constant to adjust 'strength' of scoring
    score = e(-const * pop_param * contig_param)

    return score


def score_pop(plan):
    """ Score a supplied plan for its apportionment equality. That is, check
    the population deviation of each district from the ideal average. Returns
    a standard deviation value """

    # Retrieve the number of districts in the given plan and create empty list
    # for population values from each district
    num_distrs = distr_count(plan)
    distr_pops = []

    # For each district in the plan, retrieve the nodes of that district
    # and test each node to confirm that at least one of its neighbors is
    # from the same district
    for i in range(1, num_distrs + 1):
        # Tabulate population of each district and append to list
        distr_pops.append(distr_pop(i, plan))

    # pstdev is the standard library standard deviation function for an
    # iterable input
    std_dev = pstdev(distr_pops)

    # Conditional sets a threshold for the maximum standard deviation allowed
    if std_dev > 60:
        std_dev = 160

    return std_dev


def score_contig(plan):
    """ Scores a supplied plan based on the number of contiguous districts
    present. If all are contiguous, returns 1; else, returns 0.5 ^ x, where x
    is the number of non-contiguous districts """

    num_distrs = distr_count(plan)

    # Build up a list of results for the contiguity test
    contig_list = []
    for i in range(1, num_distrs + 1):
        contig_list.append(contig_distr(i, plan))

    # Count the number of disconnected districts
    num_discon = 0
    for item in contig_list:
        if not item:
            num_discon += 1

    score = 20 ** num_discon

    return score
