#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from reject import reject_islands
from reject import reject_by_pop
from chain import chain
from draw import distr_plot_params
from networkx import draw
from networkx import json_graph
import matplotlib.pyplot as plt

# from utils import distr_pop
# from statistics import pstdev


# from propose import transistion
# from election import election
# from election import calc_winner


# from copy import deepcopy as dc
# import networkx as nx

# from utils import contig_distr
# from utils import distr_nodes
# from score import score_plan
# from score import score_pop
# from score import score_contig

import json
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """

    S = init_graph()

    adj = json_graph.adjacency_data(S)
    with open("test-dump.json", "w") as f:
        json.dump(adj, f)

    # plans = chain(S, 250000, 0.025)

    # contiguous, reject = reject_islands(plans)
    # apport, reject2 = reject_by_pop(contiguous)
    # # reject.extend(reject2)

    # print("{} raw plans".format(len(plans)))
    # print("Kept {} clean plans".format(len(apport)))
    # print(
    #     "Rejected {} malapportioned plans and {} non-contiguous plans".format(
    #         len(reject2), len(reject)
    #     )
    # )

    # for plan in plans:
    #     distr_pops = []
    #     for distr in range(1, 5):
    #         distr_pops.append(distr_pop(distr, plan))
    #     if 0 < pstdev(distr_pops) < 100:
    #         print(
    #             "Plan {} districts have population: {} (std dev:{})".format(
    #                 1 + plans.index(plan), distr_pops, round(pstdev(distr_pops), 1)
    #             )
    #         )

    # count = 1
    # for i in apport:
    #     labs, sizes, colours = distr_plot_params(i, "pop", "purple")
    #     pos = i.graph["position"]
    #     nlist = list(S.nodes)

    #     # fig = plt.figure()

    #     draw(
    #         i,
    #         pos,
    #         labels=labs,
    #         node_list=nlist,
    #         node_color=colours,
    #         node_size=3000,
    #         font_size=36,
    #         node_shape="o",
    #     )

    #     plt.savefig("imgs/new-trans-probs-{}.pdf".format(count))
    # count += 1
    # plt.show()

    # results = election(S)
    # winners = calc_winner(results)
    # for distr in winners.items():
    #     print(distr)

    # count = 1
    # for i in contiguous:
    #     # results = election(i)
    #     # winners = calc_winner(results)
    #     # print("Results for plan {}".format(count))
    #     # for distr in winners.items():
    #     #     print(distr)
    #     count += 1

    #     labels = {}
    #     for n in nlist:
    #         labels[n] = i.nodes[n]["pop"]

    # plans, _ = reject_by_pop(plans)
    # plans, _ = reject_islands(plans)
    # print("Produced {} valid plans".format(len(plans)))


if __name__ == "__main__":
    main()
