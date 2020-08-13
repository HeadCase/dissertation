#!/usr/bin/env python
""" Source code for calculating voting totals and statistics"""

import pandas as pd

from utils import distr_count
from utils import distr_nodes


def election(graph_list, fname=None):
    """ Accepts a list of graph(s) and computes results of an elections under
    each districting plan in the list. Returns a dataframe of election results
    """

    results = {}
    i = 0
    pcount = 0

    for graph in graph_list:
        num_distrs = distr_count(graph)
        plan_id = id(graph)
        plan_label = pcount

        for distr in range(1, num_distrs + 1):
            nodes = distr_nodes(distr, graph)
            vote_circ = 0
            vote_sqre = 0
            total = 0
            for node in nodes:
                vote_circ += graph.nodes[node]["vote_circ"]
                vote_sqre += graph.nodes[node]["vote_sqre"]
                total += graph.nodes[node]["pop"]

            results[i] = [plan_id, plan_label, distr, vote_circ, vote_sqre, total]
            i += 1

        pcount += 1

    df = pd.DataFrame.from_dict(
        results,
        orient="index",
        columns=["plan_id", "plan_label", "distr", "vote_circ", "vote_sqre", "total"],
    )

    if fname:
        df.to_csv(fname)

    return df
