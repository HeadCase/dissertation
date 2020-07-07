#!/usr/bin/env python
""" Initialise graph and node attributes """

import networkx as nx


def init_graph():
    """ Initialise graph """
    gname = nx.grid_2d_graph(6, 6)
    gname.graph["state"] = "Toylandia"

    # Starting districts
    dists = {
        1: [1, 2, 3, 7, 8, 9],
        2: [4, 5, 6, 10, 11, 12],
        3: [16, 17, 18, 22, 23, 24],
        4: [13, 14, 15, 19, 20, 21],
        5: [25, 26, 27, 31, 32, 33],
        6: [28, 29, 30, 34, 35, 36],
    }

    pop = {
        1: 24,
        2: 26,
        3: 23,
        7: 23,
        8: 26,
        9: 28,
        4: 27,
        5: 23,
        6: 25,
        10: 24,
        11: 27,
        12: 24,
        16: 19,
        17: 21,
        18: 26,
        22: 25,
        23: 29,
        24: 30,
        13: 21,
        14: 26,
        15: 28,
        19: 23,
        20: 24,
        21: 28,
        25: 27,
        26: 26,
        27: 26,
        31: 23,
        32: 24,
        33: 24,
        28: 18,
        29: 22,
        30: 26,
        34: 28,
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

    # S2 = dc(S)
    # S2.nodes[9]["dist"] = 4
    # S2.nodes[8]["dist"] = 4
