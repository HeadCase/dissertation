#!/usr/bin/env python
""" Main function """

# Imports
import sys

from init import init_expanded
from chain import chain
from reject import reject_islands
from reject import reject_by_pop
from utils import remove_dups
from election import election
from log import to_json


def main():
    """ Main function """

    # Set basename for the run and initialise the first graph with the starting
    # plan
    basename = "4mil-const-pt0025-ban-ncontig-variance-fixed-distr1"
    S = init_expanded()

    # Initiate the run with the starting graph, an iteration count, constant
    # value, and log file
    plans = chain(S, 4000000, 0.0025, "logs/{}".format(basename))

    # Log results, filter out illegal plans, remove duplicates, write legal
    # plans to file, and conduct and log election results
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

        no_dups = remove_dups(apport)
        to_json(no_dups, "plans/{}.json".format(basename))
        election(no_dups, "elections/{}.csv".format(basename))


if __name__ == "__main__":
    main()
