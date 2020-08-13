#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import transistion
from score import score_plan

import pandas as pd

# from score import score_contig
# from score import score_pop

# from draw import single_plot_params
# from networkx import draw
# import matplotlib.pyplot as plt


# Markov Chain Simulation
def chain(init_plan, n, const, fname):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    # and initialise it as the current plan
    plans = [init_plan]
    curr_plan = init_plan

    # Create dict  to hold all logging data. Keys are the iteration number and
    # values hold a list of logging data
    log = {}

    while i < n:

        trans = transistion(curr_plan)
        sourceNode = trans["node"]
        prop_distr = trans["prop_distr"]
        trans_out = trans["trans_out"]
        trans_in = trans["trans_in"]

        curr_distr = curr_plan.nodes[sourceNode]["distr"]

        if prop_distr != curr_distr:
            prop_plan = dc(curr_plan)
            prop_plan.nodes[sourceNode]["distr"] = prop_distr

            score_curr = score_plan(curr_plan, const)
            score_prop = score_plan(prop_plan, const)

            alpha = min(1, ((score_prop / score_curr) * (trans_in / trans_out)))
            beta = uniform(0, 1)

            if alpha > beta:
                curr_plan = prop_plan
                plans.append(curr_plan)
                flag = "accept"
            else:
                flag = "reject"

            log[i] = [
                sourceNode,
                curr_distr,
                prop_distr,
                round(score_curr, 5),
                round(trans_in, 5),
                round(score_prop, 5),
                round(trans_out, 5),
                round(alpha, 5),
                round(beta, 5),
                flag,
            ]

        else:
            log[i] = [
                sourceNode,
                curr_distr,
                prop_distr,
                9999,
                9999,
                9999,
                9999,
                9999,
                9999,
                "reject",
            ]

        if i % 100 == 0:
            print("------ End iteration {} ------".format(i))
        i += 1

    df = pd.DataFrame.from_dict(
        log,
        orient="index",
        columns=[
            "sourceNode",
            "currDistr",
            "propDistr",
            "scoreCurr",
            "transIn",
            "scoreProp",
            "transOut",
            "alpha",
            "beta",
            "outcome",
        ],
    )

    df.to_csv(fname)

    return plans
