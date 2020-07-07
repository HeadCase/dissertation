#!/usr/bin/env python
""" Main function """

# Imports
import networkx as nx
from init import init_graph
from draw import draw
from propose import candidates
from propose import distr_threshold
from propose import get_source
from propose import get_proposal
from chain import chain


def main():
    """ Main function """

    S = init_graph()
    S.nodes[8]["dist"] = 3
    S.nodes[9]["dist"] = 3
    S.nodes[14]["dist"] = 3
    S.nodes[15]["dist"] = 3
    # plans = chain(S, 40)
    # count = 1
    # for i in plans:
    #     draw(i, "refactor-S-plan{}".format(count))
    #     count += 1

    # i = 1
    # while i < 40:
    #     sourceNode, proposalNode = candidates(S)
    #     print(
    #         "Validity src: {}, Validity prp: {}".format(
    #             distr_threshold(sourceNode, S), distr_threshold(proposalNode, S)
    #         )
    #     )
    #     i += 1

    i = 1
    while i < 40:
        sourceNode = get_source(S)
        proposalNode = get_proposal(sourceNode, S)
        print(
            "Source node: {}; Node proposed: {}; Validity: {}".format(
                sourceNode, proposalNode, distr_threshold(proposalNode, S)
            )
        )
        i += 1

    # Get neighboring nodes which belong to another district, i.e.
    # candidates for district swap

    # draw(S, "refactor-S-edit")
    # print(candidates(S))
    # draw(S, "proposal-debug")


if __name__ == "__main__":
    main()
