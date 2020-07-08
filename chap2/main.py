#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from reject import reject_islands
from draw import draw
from chain import chain


def main():
    """ Main function """

    S = init_graph()

    plans = chain(S, 2)
    reject_islands(plans)
    # print(len(plans))

    # count = 1
    # for i in plans:
    #     draw(i, "refactor-S-plan{}".format(count))
    #     print("------ Iteration {} drawn ------".format(count))
    #     count += 1

    # draw(S, "refactor-S-edit")
    # print(candidates(S))
    # draw(S, "proposal-debug")


if __name__ == "__main__":
    main()
