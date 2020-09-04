#!/usr/bin/env python
""" File containing functions to reject illegal districting plans produced by
the Markov chain """

from utils import distr_count
from utils import contig_distr


def reject_islands(plans):
    """ Accepts a plans list, containing a series of graphs of possible
    districting plans, and rejects any plans where at least one district is
    non-contiguous (i.e. has an island). Returns a list of plans with
    non-contiguous plans removed """

    clean_plans = []
    reject_plans = []

    # Get a districting plan (graph) from the list of plans
    for graph in plans:
        # Retrieve the number of districts in the given plan
        num_distrs = distr_count(graph)

        # Create an empty list to hold the boolean returns from contiguity
        # check
        graph_check = []

        # Iterate through each distract in the plan
        for distr in range(1, num_distrs + 1):
            graph_check.append(contig_distr(distr, graph))

        if False in graph_check:
            reject_plans.append(graph)
        else:
            clean_plans.append(graph)

    return clean_plans, reject_plans


def reject_by_pop(plans):
    """ Accepts a plans list, containing a series of graphs of possible
    districting plans, and rejects any plans where the population of any
    district exceeds: total population * 1/number of districts (+/- 5%).
    Returns a list of plans with non-contiguous plans removed """

    clean_plans = []
    reject_plans = []

    # Get a districting plan (graph) from the list of plans
    for graph in plans:
        # Retrieve the number of districts in the given plan
        num_distrs = distr_count(graph)

        # Create empty list to be populated with booleans for each district
        graph_check = []

        # Iterate through districts in current plan
        for i in range(1, num_distrs + 1):

            # Assume pop. balance
            distr_check = True

            nodes_in_distr = [
                node for node, attrs in graph.nodes(data=True) if attrs["distr"] == i
            ]
            total_pop = 0
            for node in nodes_in_distr:
                total_pop += graph.nodes[node]["pop"]

            # Reject if district pop. is more than +/- 5% of average district
            # pop (250)
            if total_pop > 263 or total_pop < 237:
                distr_check = False

            graph_check.append(distr_check)

        if False in graph_check:
            reject_plans.append(graph)
        else:
            clean_plans.append(graph)

    return clean_plans, reject_plans
