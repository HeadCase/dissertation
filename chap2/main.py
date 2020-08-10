#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from election import election
from election import calc_winner
from reject import reject_islands
from reject import reject_by_pop
from chain import chain

from statistics import pstdev

# from copy import deepcopy as dc
import networkx as nx
from utils import distr_pop

# from utils import contig_distr
# from utils import distr_nodes
# from score import score_plan
# from score import score_contig

import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """

    # col_map = colour_scale(all=True)
    # print(col_map[1])
    S = init_graph()

    # results = election(S)
    # winners = calc_winner(results)
    # for distr in winners.items():
    #     print(distr)

    # plans =
    chain(S, 15000, 0.25)

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


if __name__ == "__main__":
    main()


############
# Snippets #
############

# nodes_in_distr = [
#     node for node, attrs in graph.nodes(data=True) if attrs["distr"] == i
# ]
