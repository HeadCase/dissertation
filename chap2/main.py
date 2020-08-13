#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from reject import reject_islands
from reject import reject_by_pop
from chain import chain

from log import to_json
from log import from_json

from draw import distr_plot_params
from networkx import draw
import matplotlib.pyplot as plt

# from networkx import Graph
# from networkx import json_graph

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

import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """

    S = init_graph()

    plans = chain(S, 2000000, 0.04, "logs/2000000-iters-c-0pt04-stdev-thres-160.csv")

    contiguous, reject = reject_islands(plans)
    apport, reject2 = reject_by_pop(contiguous)
    # # reject.extend(reject2)

    print("{} raw plans".format(len(plans)))
    print("Kept {} clean plans".format(len(apport)))
    print(
        "Rejected {} malapportioned plans and {} non-contiguous plans".format(
            len(reject2), len(reject)
        )
    )

    to_json(apport, "plans/2000000-iters-c-0pt04-stdev-thres-160")
    # readback = from_json("function-test-dump")

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
    # for i in readback:
    #     # print(i.graph["position"])
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

    #     # plt.savefig("imgs/new-trans-probs-{}.pdf".format(count))
    #     # count += 1
    #     plt.show()

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
