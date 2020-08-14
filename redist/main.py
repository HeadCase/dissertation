#!/usr/bin/env python
""" Main function """

# Imports
from init import init_grid
from init import init_expanded
from reject import reject_islands
from reject import reject_by_pop
from chain import chain
from utils import remove_dups
from election import election

# from log import to_json

# from utils import graph_sig

from log import from_json

from draw import distr_plot_params
from networkx import draw
import matplotlib.pyplot as plt

# from networkx import Graph
# from networkx import json_graph

from utils import distr_pop
from statistics import pstdev


# from propose import transistion


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

    S = init_expanded()

    plans = chain(S, 500000, 0.04, "logs/500000-test-expand-graph.csv")

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

    for i in apport:
        labs, sizes, colours = distr_plot_params(i, "pop", "purple")
        pos = i.graph["position"]
        nlist = list(S.nodes)

        draw(
            i,
            pos,
            labels=labs,
            node_list=nlist,
            node_color=colours,
            node_size=3000,
            font_size=36,
            node_shape="o",
        )

        plt.show()

    # legal_plans = from_json("plans/2000000-iters-c-0pt04-stdev-thres-160.json")
    # uniq_lgl_plans = remove_dups(legal_plans)
    # subset = uniq_lgl_plans[:10]

    # election(uniq_lgl_plans, "elections/2mil-iter-results.csv")

    # for plan in subset:
    #     results = election(plan)
    #     winners = calc_winner(results)
    #     for distr in winners.items():
    #         print(distr)

    # count = 1
    # for plan in uniq_lgl_plans:
    #     distr_pops = []
    #     for distr in range(1, 5):
    #         distr_pops.append(distr_pop(distr, plan))
    #     if 0 < pstdev(distr_pops) <= 1:
    #         print(
    #             "Plan {} districts have population: {} (std dev:{})".format(
    #                 1 + uniq_lgl_plans.index(plan),
    #                 distr_pops,
    #                 round(pstdev(distr_pops), 1),
    #             )
    #         )

    #         labs, sizes, colours = distr_plot_params(plan, "pop", "purple")
    #         pos = plan.graph["position"]
    #         nlist = list(plan.nodes)

    #         # fig = plt.figure()

    #         draw(
    #             plan,
    #             pos,
    #             labels=labs,
    #             node_list=nlist,
    #             node_color=colours,
    #             node_size=3000,
    #             font_size=36,
    #             node_shape="o",
    #         )

    #         plt.savefig("imgs/2mil-iter-lt1-stdev-{}.pdf".format(count))
    #         count += 1

    # S = init_graph()

    # plans = chain(S, 2000000, 0.04, "logs/2000000-iters-c-0pt04-stdev-thres-160.csv")

    # contiguous, reject = reject_islands(plans)
    # apport, reject2 = reject_by_pop(contiguous)
    # # # reject.extend(reject2)

    # print("{} raw plans".format(len(plans)))
    # print("Kept {} clean plans".format(len(apport)))
    # print(
    #     "Rejected {} malapportioned plans and {} non-contiguous plans".format(
    #         len(reject2), len(reject)
    #     )
    # )

    # to_json(apport, "plans/2000000-iters-c-0pt04-stdev-thres-160")
    # readback = from_json("function-test-dump")

    # count = 1
    # for i in contiguous:
    #     # results = election(i)
    #     # winners = calc_winner(results)
    #     # print("Results for plan {}".format(count))
    #     # for distr in winners.items():
    #     #     print(distr)
    #     count += 1


if __name__ == "__main__":
    main()

# Plotting

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
