#!/usr/bin/env python
""" Propose source and candidate nodes for district swap """

# Imports
from random import randint as rint


def candidates(graph):
    """ Proposal function for random walk """

    # Acquire source node from which to walk, using a while loop to condition
    # the number of nodes in the source node's district

    candNodes = []
    while candNodes == []:

        sourceNode = 0
        while sourceNode == 0:
            sourceNode = rint(1, 36)
            # print('Proposed source node: {}'.format(sourceNode))
            if not distr_threshold(sourceNode, graph):
                # print("Node {}'s district has too many
                # nodes".format(sourceNode))
                sourceNode = 0

        # Get neighbors to that node
        neighbors = [n for n in graph.neighbors(sourceNode)]

        # Get neighboring nodes which belong to another district, i.e.
        # candidates for district swap
        candNodes = [
            n
            for n in neighbors
            if graph.nodes[n]["dist"] != graph.nodes[sourceNode]["dist"]
        ]

        # print('Proposed candidate node(s): {}'.format(candNodes))

        # In order to preserve all six districts and minimise districting
        # plans with imbalanced populations, we restrict candidate nodes to
        # have between five and seven nodes
        if candNodes:
            for node in candNodes:
                if not distr_threshold(node, graph):
                    # print('Candidate {} removed'.format(node))
                    candNodes.remove(node)

    return sourceNode, candNodes


def distr_threshold(node, graph):
    """ Determine if a supplied district has too many or too few nodes """
    distr = graph.nodes[node]["dist"]
    nodes_in_dist = [
        node for node, attrs in graph.nodes(data=True) if attrs["dist"] == distr
    ]
    node_count = len(nodes_in_dist)
    if node_count > 7 or node_count < 5:
        # print("False: {} in district".format(node_count))
        return False
    else:
        # print("True: {} in district".format(node_count))
        return True
