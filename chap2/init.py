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

    vote_circ = {
        1: 18,
        2: 13,
        3: 15,
        7: 11,
        8: 14,
        9: 18,
        13: 11,
        14: 12,
        15: 17,
        4: 13,
        5: 12,
        6: 12,
        10: 13,
        11: 12,
        12: 19,
        16: 16,
        17: 14,
        18: 16,
        19: 16,
        20: 15,
        21: 13,
        25: 15,
        26: 16,
        27: 11,
        31: 11,
        32: 15,
        33: 14,
        22: 12,
        23: 15,
        24: 16,
        28: 13,
        29: 10,
        30: 14,
        34: 18,
        35: 14,
        36: 12,
    }

    vote_sqre = {
        1: 16,
        2: 13,
        3: 13,
        7: 14,
        8: 12,
        9: 10,
        13: 13,
        14: 14,
        15: 16,
        4: 13,
        5: 14,
        6: 10,
        10: 11,
        11: 13,
        12: 14,
        16: 12,
        17: 16,
        18: 20,
        19: 17,
        20: 12,
        21: 15,
        25: 12,
        26: 14,
        27: 15,
        31: 13,
        32: 13,
        33: 13,
        22: 13,
        23: 14,
        24: 14,
        28: 15,
        29: 12,
        30: 12,
        34: 16,
        35: 17,
        36: 13,
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

    # Load up population values into node attribute
    for keys, values in pop.items():
        gname.nodes[keys]["pop"] = values

    for keys, values in vote_circ.items():
        gname.nodes[keys]["vote_circ"] = values

    for keys, values in vote_sqre.items():
        gname.nodes[keys]["vote_sqre"] = values

    gname.graph["position"] = pos

    return gname
