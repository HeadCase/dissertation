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

    # Iterate over each graph in the list
    for graph in graph_list:
        num_distrs = distr_count(graph)
        plan_id = id(graph)
        plan_label = pcount

        # Iterate over each district in the graph
        for distr in range(1, num_distrs + 1):
            nodes = distr_nodes(distr, graph)
            vote_circ = 0
            vote_sqre = 0
            total = 0

            # Access individual nodes for their variable values and use them to
            # calculate district totals
            for node in nodes:
                vote_circ += graph.nodes[node]["vote_circ"]
                vote_sqre += graph.nodes[node]["vote_sqre"]
                total += graph.nodes[node]["pop"]

            # Each district result becomes an entry in a dictionary which gets
            # converted to a dataframe
            results[i] = [plan_id, plan_label, distr, vote_circ, vote_sqre, total]
            i += 1

        pcount += 1

    # Convert results dictionary to a dataframe of all election results
    df = pd.DataFrame.from_dict(
        results,
        orient="index",
        columns=["plan_id", "plan_label", "distr", "vote_circ", "vote_sqre", "total"],
    )

    # Write election results to specified file
    if fname:
        df.to_csv(fname)

    return df
