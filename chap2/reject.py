#!/usr/bin/env python
""" File containing functions to reject districting plans produced by the
Markov chain """


def reject_islands(plans):
    """ Accepts a plans list, containing a series of graphs of possible
    districting plans, and rejects any plans where at least one district is
    non-contiguous (i.e. has an island)"""

    for graph in plans:
        num_distrs = distr_count(graph)
        for i in range(1, num_distrs + 1):
            nodes_in_distr = [
                node for node, attrs in graph.nodes(data=True) if attrs["dist"] == i
            ]
            print("District {}: {} ".format(i, nodes_in_distr))


def distr_count(graph):
    """ Function to retrieve the number of districts present in a supplied
    graph """

    distrs = []
    for _, values in graph.nodes.data():
        distrs.append(values["dist"])

    count = set(distrs)
    count = len(count)
    return count


def reject_by_pop():
    pass
