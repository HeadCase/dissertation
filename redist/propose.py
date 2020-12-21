#!/usr/bin/env python
""" Generate proposals for Markov chain """

# Imports
from random import randint as rint


def transition(graph):
    """ Computes transition of a random source node to a new district and
    returns the proposed new district, the node, and its transition
    probabilities in both directions """

    # Acquire a source node at random from the full set of available nodes and
    # produce a list of districts of its neighbouring nodes
    ncount = len(list(graph.nodes))
    sourceNode = rint(1, ncount)
    nbors = list(graph.neighbors(sourceNode))
    nbors_distrs = []
    for node in nbors:
        nbors_distrs.append(graph.nodes[node]["distr"])

    # Log the current and proposed new districts for computing transition
    # probabilities and sending forward to acceptance probability
    cur_distr = graph.nodes[sourceNode]["distr"]
    prop_distr = nbors_distrs[rint(0, len(nbors_distrs) - 1)]

    # Compute 'outbound' transition probability as number of neighbours in the
    # proposed district over the total number of neighbours
    #
    # Compute 'inbound' transition as the number of neighbours in the original
    # source district over the total number of neighbors
    trans_out = nbors_distrs.count(prop_distr) / len(nbors)
    trans_in = nbors_distrs.count(cur_distr) / len(nbors)

    trans = {
        "node": sourceNode,
        "prop_distr": prop_distr,
        "trans_out": trans_out,
        "trans_in": trans_in,
    }

    return trans
