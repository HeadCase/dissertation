#!/usr/bin/env python
"""
File: toy-example.py
Author: G. W. Headley
Email: mm19gwh@leeds.ac.uk
Github: https://github.com/HeadCase
Description: Source code for example MCMC/redistricting example in
introductory MCMC chapter
"""

# Imports
import networkx as nx
from copy import deepcopy as dc

# Initialise starting graph. 6x6 for 36 voting blocks (nodes), into which we
# will put an average of 25 persons for a total voting population of 900. Each
# district should have 150 persons
S = nx.grid_2d_graph(6, 6)
S.graph["state"] = "Toylandia"

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
nx.relabel_nodes(S, mapping, copy=False)

# Load up districts into node attribute
for keys, values in dists.items():
    for node in values:
        S.nodes[node]["dist"] = keys

# Load up population values into node attribute
for keys, values in pop.items():
    S.nodes[keys]["pop"] = values


S.graph["position"] = pos

total_pop = 0
for nodes, attrs in S.nodes(data=True):
    total_pop += attrs["pop"]

# Graphing


def draw(graph):
    """Function to parse graph and plot it"""

    colour = []
    pos = S.graph["position"]

    for node in graph.nodes():
        colour.append(graph.nodes[node]["dist"])

    n = nx.draw_networkx_nodes(
        graph, pos, node_color=colour, node_size=700, with_labels=True
    )
    e = nx.draw_networkx_edges(graph, pos, with_labels=True)
    l = nx.draw_networkx_labels(graph, pos)


S2 = dc(S)
S2.nodes[1]["dist"] = 1
draw(S2)

############
# Snippets #
############

# Get nodes for a given district. Can be modified for selecting nodes based on
# any node attribute
dist1 = [node for node, attrs in S.nodes(data=True) if attrs["dist"] == 1]
