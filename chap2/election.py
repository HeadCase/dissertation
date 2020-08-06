#!/usr/bin/env python
""" Source code for calculating voting totals and statistics"""

from utils import distr_count
from utils import distr_nodes


def election(plan):
    """ Accepts a districting plan and computes results of an election under
    that plan """

    num_distrs = distr_count(plan)

    results = {
        "District 1": {"circles": 0, "squares": 0, "total": 0},
        "District 2": {"circles": 0, "squares": 0, "total": 0},
        "District 3": {"circles": 0, "squares": 0, "total": 0},
        "District 4": {"circles": 0, "squares": 0, "total": 0},
    }

    for distr in range(1, num_distrs + 1):
        nodes = distr_nodes(distr, plan)
        for node in nodes:
            results["District {}".format(distr)]["circles"] += plan.nodes[node][
                "vote_circ"
            ]
            results["District {}".format(distr)]["squares"] += plan.nodes[node][
                "vote_sqre"
            ]
            results["District {}".format(distr)]["total"] += plan.nodes[node]["pop"]

    return results


def calc_winner(results):
    """ Accepts dictionary of results and produces dictionary of winner by
    district """

    num_distrs = len(results)

    winners = {"District 1": {}, "District 2": {}, "District 3": {}, "District 4": {}}
    for distr in range(1, num_distrs + 1):
        total = results["District {}".format(distr)]["total"]
        circ_pct = results["District {}".format(distr)]["circles"] / total
        sqre_pct = results["District {}".format(distr)]["squares"] / total
        if circ_pct > sqre_pct:
            winners["District {}".format(distr)]["winner"] = "circles"
            winners["District {}".format(distr)]["percentage"] = circ_pct
        else:
            winners["District {}".format(distr)]["winner"] = "squares"
            winners["District {}".format(distr)]["percentage"] = sqre_pct

    return winners
