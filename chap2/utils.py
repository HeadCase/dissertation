#!/usr/bin/env python
""" Source code of utility functions used across the application """


def distr_count(graph):
    """ Function to retrieve the number of districts present in a supplied
    graph """

    distrs = []
    for _, values in graph.nodes.data():
        distrs.append(values["distr"])

    count = set(distrs)
    count = len(count)
    return count


def distr_pop(distr, graph):
    """ Tabulates the number of residents in a district """

    nodes_in_distr = [
        node for node, attrs in graph.nodes(data=True) if attrs["distr"] == distr
    ]
    total_pop = 0
    for node in nodes_in_distr:
        total_pop += graph.nodes[node]["pop"]

    return total_pop
