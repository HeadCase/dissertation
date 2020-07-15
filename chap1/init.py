#!/usr/bin/env python
""" Initialise graph and node attributes """

import networkx as nx


def init_graph():
    """ Initialise graph """
    gname = nx.grid_2d_graph(6, 6)
    gname.graph["state"] = "Toylandia"

    # Starting districts
    dists = {
        1: [1, 2, 3, 7, 8, 9, 13, 14, 15],
        2: [4, 5, 6, 10, 11, 12, 16, 17, 18],
        3: [19, 20, 21, 25, 26, 27, 31, 32, 33],
        4: [22, 23, 24, 28, 29, 30, 34, 35, 36],
    }

    # Population values for each node. These are used in the Markov chain
    # acceptance test and for identifying population balanced districts

    vote_circ = {
        1: 5,
        2: 4,
        3: 5,
        7: 5,
        8: 4,
        9: 6,
        13: 4,
        14: 3,
        15: 7,
        4: 4,
        5: 3,
        6: 4,
        10: 5,
        11: 7,
        12: 6,
        16: 5,
        17: 4,
        18: 6,
        19: 5,
        20: 6,
        21: 5,
        25: 6,
        26: 5,
        27: 4,
        31: 4,
        32: 5,
        33: 6,
        22: 4,
        23: 6,
        24: 6,
        28: 3,
        29: 5,
        30: 7,
        34: 7,
        35: 4,
        36: 7,
    }

    # Fix naming (and hence position) scheme inherited from built-in graph
    # function (grid_2d_graph)
    mapping = {}
    pos = {}
    count = 1
    for i in range(0, 6):
        for j in range(0, 6):
            mapping[(i, j)] = count
            pos[count] = (i, j)
            count += 1
    nx.relabel_nodes(gname, mapping, copy=False)

    # Load up districts into node attribute
    for keys, values in dists.items():
        for node in values:
            gname.nodes[node]["distr"] = keys

    for keys, values in vote_circ.items():
        gname.nodes[keys]["vote_circ"] = values
        gname.nodes[keys]["vote_sqre"] = 10 - values

    # for keys, values in vote_sqre.items():
    #     gname.nodes[keys]["vote_sqre"] = values

    gname.graph["position"] = pos

    return gname
