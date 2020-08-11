#!/usr/bin/env python

# Imports
from copy import deepcopy as dc
from random import uniform
from propose import transistion
from score import score_plan
from score import score_contig
from score import score_pop

from draw import single_plot_params
from networkx import draw
import matplotlib.pyplot as plt


# Markov Chain Simulation
def chain(init_plan, n, const):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    # and initialise it as the current plan
    plans = [init_plan]
    curr_plan = init_plan

    while i < n:

        sourceNode, prop_distr, trans_out, trans_in = transistion(curr_plan)
        curr_distr = curr_plan.nodes[sourceNode]["distr"]
        # trans = {}
        # trans = transistion(curr_plan)
        # sourceNode = trans["node"]
        # prop_distr = trans["prop_distr"]
        # trans_out = trans["trans_out"]
        # trans_in = trans["trans_in"]

        if prop_distr != curr_distr:
            prop_plan = dc(curr_plan)
            prop_plan.nodes[sourceNode]["distr"] = prop_distr

            score_curr = score_plan(curr_plan, const)
            score_prop = score_plan(prop_plan, const)

            alpha = min(1, ((score_prop / score_curr) * (trans_in / trans_out)))
            beta = uniform(0, 1)

            # print(
            #     "pop score:{}, contig score:{}, total score:{}, Hastings:{}".format(
            #         round(score_pop(curr_plan), 3),
            #         round(score_contig(curr_plan), 6),
            #         round(score_curr, 5),
            #         alpha,
            #     )
            # )

            if alpha > beta:
                curr_plan = prop_plan
                plans.append(curr_plan)

        if i % 100 == 0:
            print("------ End iteration {} ------".format(i))
        i += 1

    return plans


# nlist = list(curr_plan.nodes)

# labs, sizes, colours = single_plot_params(curr_plan, "distr", "purple")
# pos = curr_plan.graph["position"]
# draw(
#     curr_plan,
#     pos,
#     labels=labs,
#     node_list=nlist,
#     node_color=colours,
#     node_size=3000,
#     font_size=36,
#     node_shape="o",
# )

# plt.show()

# labs, sizes, colours = single_plot_params(prop_plan, "distr", "purple")
# pos = prop_plan.graph["position"]
# draw(
#     prop_plan,
#     pos,
#     labels=labs,
#     node_list=nlist,
#     node_color=colours,
#     node_size=3000,
#     font_size=36,
#     node_shape="o",
# )

# plt.show()
