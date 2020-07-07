#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import candidates
from propose import distr_threshold


# Markov Chain Simulation
def chain(graph, n):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 0

    # Place initial graph at the start of list of graphs output by the chain
    plans = [graph]
    while i < n:
        # Candidates reset to null at start of each loop
        # candNodes = []
        # sourceNode = 0
        print(id(graph))

        sourceNode, proposalNode = candidates(graph)
        srcDistr = graph.nodes[sourceNode]["dist"]
        print(
            "Validity src: {}, Validity prp: {}".format(
                distr_threshold(sourceNode, graph), distr_threshold(proposalNode, graph)
            )
        )

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

        i += 1
        # print("End of iteration {}".format(i))

    return plans
