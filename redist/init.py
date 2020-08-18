#!/usr/bin/env python
""" Initialise graph and node attributes """

import networkx as nx


def init_grid():
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
        16: 13,
        17: 12,
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
        16: 15,
        17: 18,
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

    # Dicts for margins for each party to be tabulated below
    sqre_marg = {}
    circ_marg = {}

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
    for key, value in dists.items():
        for node in value:
            gname.nodes[node]["distr"] = key

    # Load up population value into node attribute
    for key, value in pop.items():
        sqre = vote_sqre[key]
        circ = vote_circ[key]
        gname.nodes[key]["pop"] = value

        # Define margins of victory by first computing proportion of the vote
        # and subtracting other party's margin
        sqre_marg[key] = round(((sqre / value) - (circ / value)) * 100, 1)
        circ_marg[key] = round(((circ / value) - (sqre / value)) * 100, 1)

    for key, value in vote_circ.items():
        gname.nodes[key]["vote_circ"] = value

    for key, value in circ_marg.items():
        gname.nodes[key]["circ_marg"] = value

    for key, value in vote_sqre.items():
        gname.nodes[key]["vote_sqre"] = value

    for key, value in sqre_marg.items():
        gname.nodes[key]["sqre_marg"] = value

    for n in list(gname.nodes):
        gname.nodes[n]["node label"] = n

    gname.graph["position"] = pos

    return gname


def init_expanded():
    """ Initialise expanded graph with 60 nodes and six districts. This graph
    seeks to mimic a real state, so while initialised using networkx's 2d
    graph, nodes are deleted to give a non-grid shape. Districts, vote totals,
    population, etc. variables are added after the shape and labels are
    correctly defined for the nodes"""

    # 2d graph to then delete from to give shape
    graph = nx.grid_2d_graph(11, 9)

    # Remap node names to simple integer labels and adjust position to fit on a
    # simple Cartesian grid
    mapping = {}
    pos = {}
    count = 1
    for j in range(0, 9):
        for i in range(0, 11):
            mapping[(i, j)] = count
            pos[count] = (i, j)
            count += 1
    nx.relabel_nodes(graph, mapping, copy=False)

    graph.graph["position"] = pos

    # Delete nodes to give shape
    rm_list = [
        1,
        5,
        6,
        9,
        10,
        11,
        12,
        20,
        21,
        22,
        23,
        32,
        33,
        34,
        45,
        46,
        56,
        57,
        66,
        67,
        72,
        73,
        76,
        77,
        78,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
    ]

    graph.remove_nodes_from(rm_list)

    # Sequential integer labels have been messed up by deletion so remap them
    mapping = {
        2: 1,
        3: 2,
        4: 3,
        7: 4,
        8: 5,
        13: 6,
        14: 7,
        15: 8,
        16: 9,
        17: 10,
        18: 11,
        19: 12,
        24: 13,
        25: 14,
        26: 15,
        27: 16,
        28: 17,
        29: 18,
        30: 19,
        31: 20,
        35: 21,
        36: 22,
        37: 23,
        38: 24,
        39: 25,
        40: 26,
        41: 27,
        42: 28,
        43: 29,
        44: 30,
        47: 31,
        48: 32,
        49: 33,
        50: 34,
        51: 35,
        52: 36,
        53: 37,
        54: 38,
        55: 39,
        58: 40,
        59: 41,
        60: 42,
        61: 43,
        62: 44,
        63: 45,
        64: 46,
        65: 47,
        68: 48,
        69: 49,
        70: 50,
        71: 51,
        74: 52,
        75: 53,
        79: 54,
        80: 55,
        81: 56,
        82: 57,
        90: 58,
        91: 59,
        92: 60,
    }

    pos2 = {}
    for key, value in mapping.items():
        pos2[value] = pos[key]

    graph.graph["position"] = pos2
    nx.relabel_nodes(graph, mapping, copy=False)

    # District assignments
    dists = {
        1: [1, 2, 3, 6, 7, 8, 9, 10, 15, 16],
        2: [4, 5, 11, 12, 19, 20, 27, 28, 29, 30],
        3: [17, 18, 24, 25, 26, 34],
        4: [13, 14, 21, 22, 23, 31, 32, 40, 49],
        5: [35, 36, 37, 38, 39, 45, 46, 47, 52, 53],
        6: [33, 41, 42, 43, 44, 48, 50, 51, 54, 55, 56, 57, 58, 59, 60],
    }

    # Population values for each node. These are used in the Markov chain
    # acceptance test and for identifying population balanced districts
    # Ordering of dictionary is based off districting assignments
    pop = {
        1: 19,
        2: 16,
        3: 12,
        6: 21,
        7: 22,
        8: 28,
        9: 31,
        10: 36,
        15: 28,
        16: 37,
        4: 23,
        5: 17,
        11: 32,
        12: 22,
        19: 33,
        20: 24,
        27: 29,
        28: 26,
        29: 22,
        30: 22,
        17: 44,
        18: 39,
        24: 43,
        25: 48,
        26: 35,
        34: 41,
        13: 20,
        14: 29,
        21: 21,
        22: 31,
        23: 42,
        31: 25,
        32: 36,
        40: 26,
        49: 20,
        35: 40,
        36: 35,
        37: 25,
        38: 20,
        39: 21,
        45: 30,
        46: 23,
        47: 14,
        52: 23,
        53: 19,
        33: 23,
        41: 17,
        42: 19,
        43: 22,
        44: 28,
        48: 13,
        50: 15,
        51: 17,
        54: 16,
        55: 15,
        56: 14,
        57: 16,
        58: 11,
        59: 12,
        60: 12,
    }

    vote_circ = {
        1: 7,
        2: 4,
        3: 3,
        6: 10,
        7: 9,
        8: 13,
        9: 16,
        10: 21,
        15: 13,
        16: 21,
        4: 11,
        5: 7,
        11: 17,
        12: 8,
        19: 17,
        20: 11,
        27: 16,
        28: 13,
        29: 10,
        30: 11,
        17: 24,
        18: 21,
        24: 27,
        25: 29,
        26: 18,
        34: 22,
        13: 8,
        14: 16,
        21: 10,
        22: 17,
        23: 24,
        31: 13,
        32: 21,
        40: 13,
        49: 8,
        35: 24,
        36: 20,
        37: 13,
        38: 9,
        39: 9,
        45: 17,
        46: 12,
        47: 5,
        52: 10,
        53: 10,
        33: 12,
        41: 10,
        42: 11,
        43: 12,
        44: 16,
        48: 4,
        50: 8,
        51: 9,
        54: 7,
        55: 7,
        56: 4,
        57: 5,
        58: 4,
        59: 5,
        60: 6,
    }

    vote_sqre = {
        1: 12,
        2: 12,
        3: 9,
        6: 11,
        7: 13,
        8: 15,
        9: 15,
        10: 15,
        15: 15,
        16: 16,
        4: 12,
        5: 10,
        11: 15,
        12: 14,
        19: 16,
        20: 13,
        27: 13,
        28: 13,
        29: 12,
        30: 11,
        17: 20,
        18: 18,
        24: 16,
        25: 19,
        26: 17,
        34: 19,
        13: 12,
        14: 13,
        21: 11,
        22: 14,
        23: 18,
        31: 12,
        32: 15,
        40: 13,
        49: 12,
        35: 16,
        36: 15,
        37: 12,
        38: 11,
        39: 12,
        45: 13,
        46: 11,
        47: 9,
        52: 13,
        53: 9,
        33: 11,
        41: 7,
        42: 8,
        43: 10,
        44: 12,
        48: 9,
        50: 7,
        51: 8,
        54: 9,
        55: 8,
        56: 10,
        57: 11,
        58: 7,
        59: 7,
        60: 6,
    }

    # Dicts for margins for each party to be tabulated below
    sqre_marg = {}
    circ_marg = {}

    # Load up districts into node attribute
    for key, value in dists.items():
        for node in value:
            graph.nodes[node]["distr"] = key

    # Load up population value into node attribute
    for key, value in pop.items():
        sqre = vote_sqre[key]
        circ = vote_circ[key]
        graph.nodes[key]["pop"] = value

        # Define margins of victory by first computing proportion of the vote
        # and subtracting other party's margin
        sqre_marg[key] = round(((sqre / value) - (circ / value)) * 100, 1)
        circ_marg[key] = round(((circ / value) - (sqre / value)) * 100, 1)

    for key, value in vote_circ.items():
        graph.nodes[key]["vote_circ"] = value

    for key, value in circ_marg.items():
        graph.nodes[key]["circ_marg"] = value

    for key, value in vote_sqre.items():
        graph.nodes[key]["vote_sqre"] = value

    for key, value in sqre_marg.items():
        graph.nodes[key]["sqre_marg"] = value

    for n in list(graph.nodes):
        graph.nodes[n]["node label"] = n

    return graph


def gerry(graph):
    """ Accepts freshly initiated expanded graph and alters districts
    assignments to square-favouring gerrymander """

    graph.nodes[1]["distr"] = 4
    graph.nodes[2]["distr"] = 1
    graph.nodes[3]["distr"] = 1
    graph.nodes[4]["distr"] = 2
    graph.nodes[5]["distr"] = 2
    graph.nodes[6]["distr"] = 4
    graph.nodes[7]["distr"] = 1
    graph.nodes[8]["distr"] = 1
    graph.nodes[9]["distr"] = 1
    graph.nodes[10]["distr"] = 1
    graph.nodes[11]["distr"] = 2
    graph.nodes[12]["distr"] = 2
    graph.nodes[13]["distr"] = 4
    graph.nodes[14]["distr"] = 4
    graph.nodes[15]["distr"] = 1
    graph.nodes[16]["distr"] = 1
    graph.nodes[17]["distr"] = 1
    graph.nodes[18]["distr"] = 2
    graph.nodes[19]["distr"] = 2
    graph.nodes[20]["distr"] = 2
    graph.nodes[21]["distr"] = 4
    graph.nodes[22]["distr"] = 4
    graph.nodes[23]["distr"] = 3
    graph.nodes[24]["distr"] = 3
    graph.nodes[25]["distr"] = 3
    graph.nodes[26]["distr"] = 2
    graph.nodes[27]["distr"] = 2
    graph.nodes[28]["distr"] = 5
    graph.nodes[29]["distr"] = 5
    graph.nodes[30]["distr"] = 5
    graph.nodes[31]["distr"] = 4
    graph.nodes[32]["distr"] = 6
    graph.nodes[33]["distr"] = 6
    graph.nodes[34]["distr"] = 3
    graph.nodes[35]["distr"] = 3
    graph.nodes[36]["distr"] = 3
    graph.nodes[37]["distr"] = 5
    graph.nodes[38]["distr"] = 5
    graph.nodes[39]["distr"] = 5
    graph.nodes[40]["distr"] = 4
    graph.nodes[41]["distr"] = 6
    graph.nodes[42]["distr"] = 6
    graph.nodes[43]["distr"] = 6
    graph.nodes[44]["distr"] = 6
    graph.nodes[45]["distr"] = 5
    graph.nodes[46]["distr"] = 5
    graph.nodes[47]["distr"] = 5
    graph.nodes[48]["distr"] = 6
    graph.nodes[49]["distr"] = 4
    graph.nodes[50]["distr"] = 4
    graph.nodes[51]["distr"] = 6
    graph.nodes[52]["distr"] = 5
    graph.nodes[53]["distr"] = 5
    graph.nodes[54]["distr"] = 6
    graph.nodes[55]["distr"] = 4
    graph.nodes[56]["distr"] = 6
    graph.nodes[57]["distr"] = 6
    graph.nodes[58]["distr"] = 6
    graph.nodes[59]["distr"] = 6
    graph.nodes[60]["distr"] = 6

    return graph
