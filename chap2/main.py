#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
import networkx as nx
from reject import reject_islands
from reject import reject_by_pop
from draw import draw
from chain import chain
from utils import distr_pop
from utils import contig_distr
from utils import distr_nodes
from statistics import pstdev
from score import score_plan
from score import score_contig

import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

# from copy import deepcopy as dc


def main():
    """ Main function """

    S = init_graph()
    plans = chain(S, 2000, 0.15)
    # plans, _ = reject_islands(plans)
    plans, _ = reject_by_pop(plans)
    # print("Produced {} valid plans".format(len(plans)))

    # contiguous, reject = reject_islands(plans)
    # clean, reject2 = reject_by_pop(contiguous)
    # reject.extend(reject2)

    # print("{} raw plans".format(len(plans)))
    # print("Kept {} clean plans".format(len(clean)))
    # print("Rejected {} non-contiguous or malapportioned plans".format(len(reject)))

    count = 1
    for i in plans:
        draw(i, "two-factor-scoring-plan{}".format(count))
        print("------ Two Factor Score Plan {} drawn ------".format(count))
        count += 1

    for plan in plans:
        distr_pops = []
        for distr in range(1, 5):
            distr_pops.append(distr_pop(distr, plan))
        print(
            "Plan {} districts have population: {} (std dev: {})".format(
                1 + plans.index(plan), distr_pops, round(pstdev(distr_pops), 1)
            )
        )

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
