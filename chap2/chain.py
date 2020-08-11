#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import transistion
from score import score_plan


# Markov Chain Simulation
def chain(init_plan, n, const=0.2):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    # and initialise it as the current plan
    plans = [init_plan]
    curr_plan = init_plan

    while i < n:

        trans = transistion(curr_plan)
        sourceNode = trans["node"]
        prop_distr = trans["prop_distr"]
        trans_out = trans["trans_out"]
        trans_in = trans["trans_in"]

        prop_plan = dc(curr_plan)
        prop_plan.nodes[sourceNode]["distr"] = prop_distr

        score_curr = score_plan(curr_plan, const)
        score_prop = score_plan(prop_plan, const)

        alpha = min(1, (score_prop / score_curr) * (trans_in / trans_out))
        beta = uniform(0, 1)

        if alpha > beta:
            curr_plan = prop_plan
            plans.append(curr_plan)

        if i % 100 == 0:
            print("------ End iteration {} ------".format(i))
        i += 1

    return plans
