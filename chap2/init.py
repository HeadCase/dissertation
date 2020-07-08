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

    pop = {
        1: 34,
        2: 26,
        3: 28,
        7: 25,
        8: 26,
        9: 28,
        13: 24,
        14: 26,
        15: 33,
        4: 26,
        5: 26,
        6: 22,
        10: 24,
        11: 25,
        12: 33,
        16: 28,
        17: 30,
        18: 36,
        19: 33,
        20: 27,
        21: 28,
        25: 27,
        26: 30,
        27: 26,
        31: 24,
        32: 28,
        33: 27,
        22: 25,
        23: 29,
        24: 30,
        28: 28,
        29: 22,
        30: 26,
        34: 34,
        35: 31,
        36: 25,
    }
    # vote_share_cr
    # vote_share_sq

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
            gname.nodes[node]["dist"] = keys

    # Load up population values into node attribute
    for keys, values in pop.items():
        gname.nodes[keys]["pop"] = values

    gname.graph["position"] = pos

    return gname
