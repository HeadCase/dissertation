#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from election import election
from election import calc_winner
from reject import reject_islands
from reject import reject_by_pop
from draw import draw
from draw import single_plot_params
from chain import chain

from statistics import pstdev

# from copy import deepcopy as dc
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils import distr_pop

# from utils import contig_distr
# from utils import distr_nodes
# from score import score_plan
# from score import score_contig

import sys
import numpy

import matplotlib.font_manager as font_manager

mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]

numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """

    S = init_graph()
    labs, sizes, colours = single_plot_params(S, "pop", "green")
    pos = S.graph["position"]
    nlist = list(S.nodes)

    nx.draw(
        S,
        pos,
        labels=labs,
        node_list=nlist,
        node_color=colours,
        node_size=sizes,
        font_size=50,
        node_shape="s",
    )
    plt.show()

    # results = election(S)
    # winners = calc_winner(results)
    # for distr in winners.items():
    #     print(distr)

    # plans = chain(S, 15000, 0.25)

    # apport, reject = reject_by_pop(plans)
    # contiguous, reject2 = reject_islands(apport)
    # reject.extend(reject2)

    # print("{} raw plans".format(len(plans)))
    # print("Kept {} clean plans".format(len(contiguous)))
    # print(
    #     "Rejected {} malapportioned plans and {} non-contiguous plans".format(
    #         len(reject), len(reject2)
    #     )
    # )

    # count = 1
    # for i in contiguous:
    #     # results = election(i)
    #     # winners = calc_winner(results)
    #     # print("Results for plan {}".format(count))
    #     # for distr in winners.items():
    #     #     print(distr)
    #     count += 1

    #     pos = i.graph["position"]
    #     nlist = list(i.nodes)
    #     size = []
    #     colour = []

    #     for n in nlist:
    #         size.append((i.nodes[n]["pop"] ** 3) / 3)
    #         if i.nodes[n]["distr"] == 1:
    #             colour.append("#EEB653")
    #         elif i.nodes[n]["distr"] == 2:
    #             colour.append("#CE477B")
    #         elif i.nodes[n]["distr"] == 3:
    #             colour.append("#40649D")
    #         else:
    #             colour.append("#96D84B")

    #     labels = {}
    #     for n in nlist:
    #         labels[n] = i.nodes[n]["pop"]

    #     nx.draw(
    #         i,
    #         pos,
    #         labels=labels,
    #         font_size=60,
    #         node_list=nlist,
    #         node_size=size,
    #         node_shape="s",
    #         node_color=colour,
    #         linewidths=4,
    #         width=4,
    #     )
    #     plt.show()

    # plans, _ = reject_by_pop(plans)
    # plans, _ = reject_islands(plans)
    # print("Produced {} valid plans".format(len(plans)))

    # count = 1
    # for i in contiguous:
    #     draw(i, "proposal-refactor-plan{}".format(count))
    #     print("------ Proposal Refactor Plan {} drawn ------".format(count))
    #     count += 1

    # for plan in plans:
    #     distr_pops = []
    #     for distr in range(1, 5):
    #         distr_pops.append(distr_pop(distr, plan))
    #     print(
    #         "Plan {} districts have population: {} (std dev: {})".format(
    #             1 + plans.index(plan), distr_pops, round(pstdev(distr_pops), 1)
    #         )
    #     )

    # count = 1
    # for i in clean:
    #     draw(i, "meeting-test-clean-plans{}".format(count))
    #     print("------ Clean plan {} drawn ------".format(count))
    #     count += 1

    # plans = [S]
    # S2 = dc(S)
    # S2.nodes[26]["distr"] = 1
    # plans.append(S2)
    # count = 1
    # for i in reject:
    #     draw(i, "reject-plans{}".format(count))
    #     print("------ Reject {} drawn ------".format(count))
    #     count += 1

    # draw(S, "refactor-S-edit")
    # print(candidates(S))
    # draw(S, "score-refactor")
    # draw(S2, "island-test")


if __name__ == "__main__":
    main()


############
# Snippets #
############

# nodes_in_distr = [
#     node for node, attrs in graph.nodes(data=True) if attrs["distr"] == i
# ]
