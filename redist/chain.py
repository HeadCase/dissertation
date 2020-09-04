#!/usr/bin/env python

# Imports
import timeit
import pandas as pd
from time import ctime
from copy import deepcopy as dc

from random import uniform
from propose import transistion
from score import score_plan
from score import score_contig
from score import score_pop


# Markov Chain Simulation
def chain(init_plan, n, const, fname):
    """ Markov chain function for computing new redistricting plans based off
    of an initial districting, an iteration count, and a constant value """

    # While loop to control number of iterations
    i = 1

    # Place initial graph at the start of list of graphs output by the chain
    # and initialise it as the current plan
    plans = [init_plan]
    curr_plan = init_plan

    # Create dict to hold all logging data. Key is the iteration number and
    # values hold a list of logging data
    log = {}

    # Instantiate variables for logging
    score_curr = 0
    score_prop = 0
    pop_curr = 0
    pop_prop = 0
    contig_curr = 0
    contig_prop = 0
    alpha = 0
    beta = 0
    flag = ""
    lcount = 1
    start = timeit.default_timer()

    while i <= n:

        # Get a proposal using transition() function
        trans = transistion(curr_plan)

        # Extract relevant bits from the transition() return
        sourceNode = trans["node"]
        prop_distr = trans["prop_distr"]
        trans_out = trans["trans_out"]
        trans_in = trans["trans_in"]

        # Get the current source node's district assignment
        curr_distr = curr_plan.nodes[sourceNode]["distr"]

        # If the proposal and current districts are different, we have a
        # non-identical but adjacent plan, so proceed to acceptance probability
        if prop_distr != curr_distr:

            # Deep copy makes sure proposal is a new python object
            prop_plan = dc(curr_plan)
            # Set proposal district
            prop_plan.nodes[sourceNode]["distr"] = prop_distr

            # Score up both plans
            score_curr = score_plan(curr_plan, const)
            score_prop = score_plan(prop_plan, const)
            pop_curr = score_pop(curr_plan)
            pop_prop = score_pop(prop_plan)
            contig_curr = score_contig(curr_plan)
            contig_prop = score_contig(prop_plan)

            # Compute acceptance
            alpha = min(1, ((score_prop / score_curr) * (trans_in / trans_out)))
            beta = uniform(0, 1)

            # Accept or reject
            if alpha > beta:
                curr_plan = prop_plan
                plans.append(curr_plan)
                flag = "accept"
            else:
                flag = "reject"

        # If the proposal and current districts are the same, then the plans
        # are identical and we have a repeat
        else:
            flag = "repeat"

        # Push logging variables to the logging dictionary after main body of
        # iteration
        log[i] = [
            sourceNode,
            curr_distr,
            prop_distr,
            round(score_curr, 3),
            round(score_prop, 3),
            round(pop_curr, 3),
            round(pop_prop, 3),
            round(contig_curr, 3),
            round(contig_prop, 3),
            round(trans_in, 3),
            round(trans_out, 3),
            round(alpha, 3),
            round(beta, 3),
            flag,
        ]

        # Print some details of progress every 100 iterations
        if i % 100 == 0:
            stop = timeit.default_timer()
            print(
                "{} | Runtime:{:010.2f} | iter:{:.>10}".format(
                    ctime(), (stop - start), i
                )
            )

            with open("{}.txt".format(fname), "a+") as f:
                print(
                    "{} | Runtime:{:010.2f} | iter:{:.>10}".format(
                        ctime(), (stop - start), i
                    ),
                    file=f,
                )

        # Next two conditions handle the logging. Dumping the entire dictionary
        # to csv proved to produce a massive file (4 million iterations after
        # all). These conditionals dump the log dictionary to file at intervals
        # of 1/8th of the total iteration count. Splitting them up into 8
        # pieces makes for more manage file sizes

        # After the very last iteration, dump the 8th and final log piece
        if i == n:
            df = pd.DataFrame.from_dict(
                log,
                orient="index",
                columns=[
                    "sourceNode",
                    "currDistr",
                    "propDistr",
                    "scoreCurr",
                    "scoreProp",
                    "pop_curr",
                    "pop_prop",
                    "contig_curr",
                    "contig_prop",
                    "transIn",
                    "transOut",
                    "alpha",
                    "beta",
                    "outcome",
                ],
            )
            df.to_csv("{}-{}.csv".format(fname, lcount))

        # Dump the log dictionary to file after each successive 1/8th of
        # iterations is complete. Off by one for the final iteration so that's
        # handled above
        if i % (n / 8) == 0:
            df = pd.DataFrame.from_dict(
                log,
                orient="index",
                columns=[
                    "sourceNode",
                    "currDistr",
                    "propDistr",
                    "scoreCurr",
                    "scoreProp",
                    "pop_curr",
                    "pop_prop",
                    "contig_curr",
                    "contig_prop",
                    "transIn",
                    "transOut",
                    "alpha",
                    "beta",
                    "outcome",
                ],
            )

            df.to_csv("{}-{}.csv".format(fname, lcount))
            lcount += 1
            log = {}

        i += 1

    return plans
