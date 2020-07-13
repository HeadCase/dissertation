#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import candidates
from score import score_plan


# Markov Chain Simulation
def chain(init_plan, n, const=0.025):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    # and initialise it as the current plan
    plans = [init_plan]
    curr_plan = init_plan

    while i < n:

        sourceNode, proposalNode = candidates(curr_plan)
        srcDistr = curr_plan.nodes[sourceNode]["distr"]

        prop_plan = dc(curr_plan)
        prop_plan.nodes[proposalNode]["distr"] = srcDistr

        score_curr = score_plan(curr_plan, const)
        score_prop = score_plan(prop_plan, const)

        alpha = min(1, (score_prop / score_curr))
        beta = uniform(0, 1)

        if alpha > beta:
            curr_plan = prop_plan
            plans.append(curr_plan)

        print("------ End iteration {} ------".format(i))
        i += 1

    return plans
