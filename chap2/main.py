#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from draw import draw
from propose import candidates
from chain import chain


def main():
    """ Main function """

    S = init_graph()
    # draw(S, "refactor-S")
    plans = chain(S, 20)
    for i in plans:
        draw(plans[i], "refactor-S-plan{}".format(i))
    # candidates(S)
    # draw(S)


if __name__ == "__main__":
    main()
