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
# from election import election
# from statistics import pstdev

# from draw import distr_plot_params
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

    basename = "5mil-const-pt0025-ban-ncontig-variance-distr1-fix"
    S = init_expanded()

    plans = chain(S, 5000000, 0.0025, "logs/{}".format(basename))

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

    # uniq_lgl_plans = from_json("plans/{}.json".format(basename))
    # # election(uniq_lgl_plans, "elections/{}.csv".format(basename))

    # count = 1
    # for plan in uniq_lgl_plans:
    #     distr_pops = []
    #     dcnt = distr_count(plan)
    #     for distr in range(1, dcnt + 1):
    #         distr_pops.append(distr_pop(distr, plan))
    #     if 0 < pstdev(distr_pops) <= 5:
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

    #         plt.figure(figsize=(19, 15))

    #         draw(
    #             plan,
    #             pos,
    #             labels=labs,
    #             node_list=nlist,
    #             node_color=colours,
    #             node_size=sizes,
    #             font_size=36,
    #             node_shape="o",
    #         )

    #         plt.savefig("imgs/{}-{}.pdf".format(basename, count))
    #         count += 1


if __name__ == "__main__":
    main()
