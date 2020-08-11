#!/usr/bin/env python
""" Propose source and candidate nodes for district swap """

# Imports
from random import randint as rint

# from utils import distr_nodes


def transistion(graph):
    """ Computes transition of a random source node to a new district and
    returns the proposed new district, the node, and its transition
    probabilities in both directions """

    # Acquire a source node at random from the full set of available nodes and
    # produce a list of districts of its neighbouring nodes
    sourceNode = rint(1, 36)
    nbors = list(graph.neighbors(sourceNode))
    nbors_distrs = []
    for node in nbors:
        nbors_distrs.append(graph.nodes[node]["distr"])

    # Log the current and proposed new districts to computing transition
    # probabilities
    cur_distr = graph.nodes[sourceNode]["distr"]
    prop_distr = nbors_distrs[rint(0, len(nbors_distrs) - 1)]

    # Compute 'outbound' transition probability as count of nodes which are in
    # the same district as the proposed district from all neighbours over the
    # total number of neighbours
    trans_out = nbors_distrs.count(prop_distr) / len(nbors)
    trans_in = nbors_distrs.count(cur_distr) / len(nbors)

    trans = {
        "node": sourceNode,
        "prop_distr": prop_distr,
        "trans_out": trans_out,
        "trans_in": trans_in,
    }

    return trans


# def candidates(graph):
#     """ Proposal function for random walk """

#     # Acquire source node from which to walk, using a while loop to condition
#     # the number of nodes in the source node's district
#     proposalNode = 0
#     while proposalNode == 0:
#         sourceNode = rint(1, 36)
#         proposalNode = get_proposal(sourceNode, graph)

#     return sourceNode, proposalNode


# def get_proposal(sourceNode, graph):
#     """ Get a proposal node neighbouring the source node, to potentially be
#     swapped to the district of the source node """
#     proposalNode = 0

#     # Get neighbors to that node
#     neighbors = list(graph.neighbors(sourceNode))

#     # Get neighboring nodes which belong to another district, i.e.
#     # candidates for district swap
#     candNodes = [
#         n
#         for n in neighbors
#         if graph.nodes[n]["distr"] != graph.nodes[sourceNode]["distr"]
#     ]

#     # In order to preserve all six districts and minimise districting
#     # plans with imbalanced populations, we restrict candidate nodes to
#     # have between five and seven nodes
#     if candNodes:
#         validNodes = []
#         for node in candNodes:
#             if proposal_threshold(node, graph):
#                 validNodes.append(node)
#         if len(validNodes) > 1:
#             pick = rint(0, len(validNodes) - 1)
#             proposalNode = validNodes[pick]
#         elif len(validNodes) == 1:
#             proposalNode = validNodes[0]

#     return proposalNode


# def proposal_threshold(node, graph):
#     """ Determine if a supplied district has too many or too few nodes """
#     distr = graph.nodes[node]["distr"]
#     nodes = distr_nodes(distr, graph)
#     node_count = len(nodes)

#     # node_count = 0
#     # for _, attrs in graph.nodes(data=True):
#     #     if attrs["distr"] == distr:
#     #         node_count += 1
#     if node_count < 2:
#         return False
#     else:
#         return True


# def source_threshold(node, graph):
#     """ Determine if a supplied district has too many or too few nodes """
#     distr = graph.nodes[node]["distr"]
#     node_count = 0
#     for _, attrs in graph.nodes(data=True):
#         if attrs["distr"] == distr:
#             node_count += 1
#     if node_count > 10:
#         return False
#     else:
#         return True
