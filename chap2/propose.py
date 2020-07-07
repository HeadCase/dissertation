#!/usr/bin/env python
""" Propose source and candidate nodes for district swap """

# Imports
from random import randint as rint


def candidates(graph):
    """ Proposal function for random walk """

    # Acquire source node from which to walk, using a while loop to condition
    # the number of nodes in the source node's district
    sourceNode = get_source(graph)
    proposalNode = get_proposal(sourceNode, graph)

    return sourceNode, proposalNode


def get_source(graph):
    sourceNode = 0
    while sourceNode == 0:
        sourceNode = rint(1, 36)
        if not distr_threshold(sourceNode, graph):
            sourceNode = 0

    return sourceNode


def get_proposal(sourceNode, graph):
    proposalNode = 0
    candNodes = []

    __import__("pdb").set_trace()
    while proposalNode == 0:

        # Get neighbors to that node
        neighbors = list(graph.neighbors(sourceNode))

        # Get neighboring nodes which belong to another district, i.e.
        # candidates for district swap
        candNodes = [
            n
            for n in neighbors
            if graph.nodes[n]["dist"] != graph.nodes[sourceNode]["dist"]
        ]

        # In order to preserve all six districts and minimise districting
        # plans with imbalanced populations, we restrict candidate nodes to
        # have between five and seven nodes
        if candNodes:
            for node in candNodes:
                if not distr_threshold(node, graph):
                    candNodes.remove(node)
            if len(candNodes) > 1:
                pick = rint(0, len(candNodes) - 1)
                proposalNode = candNodes[pick]
            elif len(candNodes) == 1:
                proposalNode = candNodes[0]

    return proposalNode


def distr_threshold(node, graph):
    """ Determine if a supplied district has too many or too few nodes """
    distr = graph.nodes[node]["dist"]
    node_count = 0
    for node, attrs in graph.nodes(data=True):
        if attrs["dist"] == distr:
            node_count += 1
    if node_count <= 5:
        return False
    else:
        return True
