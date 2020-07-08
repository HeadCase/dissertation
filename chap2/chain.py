#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import candidates


# Markov Chain Simulation
def chain(graph, n):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    plans = [graph]
    while i < n:

        sourceNode, proposalNode = candidates(graph)
        srcDistr = graph.nodes[sourceNode]["dist"]

        score_source = graph.nodes[sourceNode]["pop"]
        q_source = 1 / len(graph.adj[sourceNode])
        score_prop = graph.nodes[proposalNode]["pop"]
        q_prop = 1 / len(graph.adj[proposalNode])

        alpha = min(1, (score_prop / score_source) * (q_prop / q_source))
        beta = uniform(0.5, 1)

        if alpha > beta:
            update = dc(graph)
            update.nodes[proposalNode]["dist"] = srcDistr
            graph = update
            plans.append(graph)

        print("------ End iteration {} ------".format(i))
        i += 1

    return plans
