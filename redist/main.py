#!/usr/bin/env python
""" Main function """

# Imports
from init import init_expanded
from reject import reject_islands
from reject import reject_by_pop
from chain import chain
from log import to_json
from utils import remove_dups

# from log import from_json
# from utils import distr_pop
# from utils import distr_count
# from draw import distr_plot_params
# from election import election

# from statistics import pstdev
# from networkx import draw
# import matplotlib.pyplot as plt
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


# from networkx import json_graph
# from init import init_grid
# from utils import graph_sig
# from networkx import Graph
# from propose import transistion
# from copy import deepcopy as dc
# import networkx as nx
# from utils import contig_distr
# from utils import distr_nodes
# from score import score_plan
# from score import score_pop
# from score import score_contig


def main():
    """ Main function """

    basename = "4mil-const00pt25-ban-ncontig-variance"
    S = init_expanded()

    plans = chain(S, 4000000, 0.0025, "logs/{}".format(basename))

    with open("logs/{}.txt".format(basename), "a+") as f:
        sys.stdout = f
        print("\nRun complete.\n")

        contiguous, reject = reject_islands(plans)
        apport, reject2 = reject_by_pop(contiguous)

        print("{} raw plans".format(len(plans)))
        print("Kept {} clean plans".format(len(apport)))
        print(
            "Rejected {} malapportioned plans and {} non-contiguous plans".format(
                len(reject2), len(reject)
            )
        )

        remove_dups(apport)

        to_json(apport, "plans/{}.json".format(basename))

    # plans = chain(
    #     S, 1000000, 0.0025, "logs/1000000-iters-exp-graph-working-params-full-log.csv"
    # )

    # # reject.extend(reject2)

    # to_json(apport, "plans/1000000-iters-exp-graph-working-params.json")

    # legal_plans = from_json("plans/1000000-iters-exp-graph-working-params.json")
    # uniq_lgl_plans = remove_dups(legal_plans)

    # election(uniq_lgl_plans, "elections/1mil-iters-exp-graph.csv")

    # # count = 1
    # for plan in uniq_lgl_plans:
    #     distr_pops = []
    #     dcnt = distr_count(plan)
    #     for distr in range(1, dcnt + 1):
    #         distr_pops.append(distr_pop(distr, plan))
    #     if 0 < pstdev(distr_pops) <= 7:
    #         print(
    #             "Plan {} districts have population: {} (std dev:{})".format(
    #                 1 + uniq_lgl_plans.index(plan),
    #                 distr_pops,
    #                 round(pstdev(distr_pops), 1),
    #             )
    #         )

    # labs, sizes, colours = distr_plot_params(plan, "pop", "purple")
    # pos = plan.graph["position"]
    # nlist = list(plan.nodes)

    # plt.figure(figsize=(19, 15))

    # draw(
    #     plan,
    #     pos,
    #     labels=labs,
    #     node_list=nlist,
    #     node_color=colours,
    #     node_size=sizes,
    #     font_size=36,
    #     node_shape="o",
    # )

    # plt.savefig("imgs/100k-iters-exp-graph-good-params-{}.pdf".format(count))
    # count += 1

    # S = init_graph()

    # plans = chain(S, 2000000, 0.04, "logs/2000000-iters-c-0pt04-stdev-thres-160.csv")

    # contiguous, reject = reject_islands(plans)
    # apport, reject2 = reject_by_pop(contiguous)
    # # # reject.extend(reject2)

    # for plan in subset:
    #     results = election(plan)
    #     winners = calc_winner(results)
    #     for distr in winners.items():
    #         print(distr)

    # print("{} raw plans".format(len(plans)))
    # print("Kept {} clean plans".format(len(apport)))
    # print(
    #     "Rejected {} malapportioned plans and {} non-contiguous plans".format(
    #         len(reject2), len(reject)
    #     )
    # )

    # to_json(apport, "plans/2000000-iters-c-0pt04-stdev-thres-160")
    # readback = from_json("function-test-dump")


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
