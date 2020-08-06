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
from random import randint as rint
from random import uniform
import matplotlib.pyplot as plt

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

S2 = dc(S)
S2.nodes[9]["dist"] = 4
S2.nodes[8]["dist"] = 4


def candidates(graph):
    """ Proposal function for random walk """

    # Acquire source node from which to walk, using a while loop to condition
    # the number of nodes in the source node's district

    candNodes = []
    while candNodes == []:

        sourceNode = 0
        while sourceNode == 0:
            sourceNode = rint(1, 36)
            # print('Proposed source node: {}'.format(sourceNode))
            if not distr_threshold(sourceNode, graph):
                # print("Node {}'s district has too many nodes".format(sourceNode))
                sourceNode = 0

        # Get neighbors to that node
        neighbors = [n for n in graph.neighbors(sourceNode)]

        # Get neighboring nodes which belong to another district, i.e.
        # candidates for district swap
        candNodes = [
            n
            for n in neighbors
            if graph.nodes[n]["dist"] != graph.nodes[sourceNode]["dist"]
        ]

        # print('Proposed candidate node(s): {}'.format(candNodes))

        # In order to preserve all six districts and minimise districting
        # plans with imbalanced populations, we restrict candidate nodes to
        # have between five and seven nodes
        if candNodes:
            for node in candNodes:
                if not distr_threshold(node, graph):
                    # print('Candidate {} removed'.format(node))
                    candNodes.remove(node)

    return sourceNode, candNodes


def distr_threshold(node, graph):
    """ Determine if a supplied district has too many or too few nodes """
    distr = graph.nodes[node]["dist"]
    nodes_in_dist = [
        node for node, attrs in graph.nodes(data=True) if attrs["dist"] == distr
    ]
    node_count = len(nodes_in_dist)
    if node_count > 7 or node_count < 5:
        # print("False: {} in district".format(node_count))
        return False
    else:
        # print("True: {} in district".format(node_count))
        return True


candidates(S2)


# Markov Chain Simulation
def chain(graph, n):
    """ Markov chain function"""

    # While loop to control number of iterations
    i = 0

    # Place initial graph at the start of list of graphs output by the chain
    plans = [graph]
    while i < n:
        # Candidates reset to null at start of each loop
        candNodes = []
        sourceNode = 0

        # Get proposal node for potential district change. candidates()
        # function can return empty list (node that has no neighbours from
        # other districts), so we loop until we get a non-empty list
        # while candNodes == []:
        sourceNode, candNodes = candidates(graph)
        if len(candNodes) > 1:
            pick = rint(0, len(candNodes) - 1)
            proposal = candNodes[pick]
        else:
            proposal = candNodes[0]

        print("Graph source validity: {}".format(distr_threshold(sourceNode, graph)))
        print("Graph proposal validity: {}".format(distr_threshold(proposal, graph)))
        print("--------------------------")

        # print(
        #     "Source node ({}) validity: {}, Candidate node ({}) validity: {}".format(
        #         sourceNode,
        #         distr_threshold(sourceNode, graph),
        #         proposal,
        #         distr_threshold(proposal, graph),
        #     )
        # )

        score_source = graph.nodes[sourceNode]["pop"]
        q_source = 1 / len(graph.adj[sourceNode])
        score_prop = graph.nodes[proposal]["pop"]
        q_prop = 1 / len(graph.adj[proposal])

        alpha = min(1, (score_prop / score_source) * (q_prop / q_source))
        beta = uniform(0.5, 1)

        if alpha > beta:
            update = dc(graph)
            print(
                "Update source validity: {}".format(distr_threshold(sourceNode, update))
            )
            print(
                "Update proposal validity: {}".format(distr_threshold(proposal, update))
            )
            print("--------------------------")
            update.nodes[proposal]["dist"] = update.nodes[sourceNode]["dist"]
            graph = update
            plans.append(graph)

        print("End of iteration {}".format(i))
        i += 1

    return plans


src, candi = candidates(S2)
print(distr_threshold(src, S2))
for i in candi:
    print(distr_threshold(i, S2))

plans = chain(S, 15)
draw(plans[41])

count = 1
for i in range(0, 8):
    draw(plans[i], "plan-{}".format(count))
    count += 1


len(S.adj[4])


# Graphing
def draw(graph, fname=None):
    """Function to parse graph and plot it"""

    colour = []
    pos = S.graph["position"]

    for node in graph.nodes():
        colour.append(graph.nodes[node]["dist"])

    nx.draw_networkx_nodes(
        graph, pos, node_color=colour, node_size=700, with_labels=True
    )
    nx.draw_networkx_edges(graph, pos, with_labels=True)
    nx.draw_networkx_labels(graph, pos)
    if fname:
        plt.savefig("imgs/{}.pdf".format(fname))


############
# Snippets #
############

# Get nodes for a given district. Can be modified for selecting nodes based on
# any node attribute
dist1 = [node for node, attrs in S.nodes(data=True) if attrs["dist"] == 1]

# nodeDist = graph.nodes[node]["dist"]
# # print("Node district: {}".format(nodeDist))
# nodes_in_dist = [
#     node
#     for node, attrs in graph.nodes(data=True)
#     if attrs["dist"] == nodeDist
# ]
# # print("Num. nodes in district: {}".format(len(nodes_in_dist)))
# if len(nodes_in_dist) < 5 or 7 < len(nodes_in_dist):
#     candNodes.remove(node)
