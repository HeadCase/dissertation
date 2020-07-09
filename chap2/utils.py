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
