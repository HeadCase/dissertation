#!/usr/bin/env python
""" Source code for scoring districting plans """

from utils import distr_count
from utils import distr_pop
from math import exp as e
from statistics import pstdev


def score_plan(plan, const=0.025):
    """ Accepts a districting plan in the form of a networkx graph and scores
    it for apportionment equality. The score function takes the form of an
    energy function using the standard deviation of the population of each
    district """

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

    # Standard library standard deviation function for iterable input
    std_dev = pstdev(distr_pops)

    # Energy function with constant to adjust 'strength' of scoring
    score = e(-const * std_dev)

    return score
