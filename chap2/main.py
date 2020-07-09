#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from reject import reject_islands
from reject import reject_by_pop
from draw import draw
from chain import chain

# from copy import deepcopy as dc


def main():
    """ Main function """

    S = init_graph()
    plans = chain(S, 10000)
    contiguous, reject = reject_islands(plans)
    clean, reject2 = reject_by_pop(contiguous)
    reject.extend(reject2)

    print("{} raw plans".format(len(plans)))
    print("Kept {} clean plans".format(len(clean)))
    print("Rejected {} non-contiguous or malapportioned plans".format(len(reject)))

    count = 1
    for i in clean:
        draw(i, "meeting-test-clean-plans{}".format(count))
        print("------ Clean plan {} drawn ------".format(count))
        count += 1

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
    # draw(S, "proposal-debug")
    # draw(S2, "island-test")


if __name__ == "__main__":
    main()


############
# Snippets #
############

# nodes_in_distr = [
#     node for node, attrs in graph.nodes(data=True) if attrs["distr"] == i
# ]
