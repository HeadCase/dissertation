#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import randint as rint
from random import uniform
from propose import candidates


# Markov Chain Simulation
def chain(graph, n):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 0

    # Place initial graph at the start of list of graphs output by the chain
    plans = [graph]
    while i < n:
        # Candidates reset to null at start of each loop
        candNodes = []
        sourceNode = 0

        # Get proposal node for potential district change. candidates()
        # function can return empty list (node that has no neighbours from
        # other districts), so we loop until we get a non-empty list
        # while candNodes == []:
        sourceNode, candNodes = candidates(graph)
        if len(candNodes) > 1:
            pick = rint(0, len(candNodes) - 1)
            proposal = candNodes[pick]
        else:
            proposal = candNodes[0]

        score_source = graph.nodes[sourceNode]["pop"]
        q_source = 1 / len(graph.adj[sourceNode])
        score_prop = graph.nodes[proposal]["pop"]
        q_prop = 1 / len(graph.adj[proposal])

        alpha = min(1, (score_prop / score_source) * (q_prop / q_source))
        beta = uniform(0.5, 1)

        if alpha > beta:
            update = dc(graph)
            update.nodes[proposal]["dist"] = update.nodes[sourceNode]["dist"]
            graph = update
            plans.append(graph)

        print("End of iteration {}".format(i))
        i += 1

    return plans
