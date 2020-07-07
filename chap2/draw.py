#!/usr/bin/env python
""" Drawing functions for network"""

# Imports
import networkx as nx
import matplotlib.pyplot as plt


def draw(graph, fname=None):
    """Function to parse graph and plot it"""

    colour = []
    pos = graph.graph["position"]

    for node in graph.nodes():
        colour.append(graph.nodes[node]["dist"])

    nx.draw_networkx_nodes(
        graph, pos, node_color=colour, node_size=700, with_labels=True
    )
    nx.draw_networkx_edges(graph, pos, with_labels=True)
    nx.draw_networkx_labels(graph, pos)
    if fname:
        plt.savefig("imgs/{}.pdf".format(fname))
