#!/usr/bin/env python
""" Drawing functions for network"""

# Imports
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

# Font fiddling
import matplotlib.font_manager as font_manager

mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]


def draw(graph, fname=None, colour=None):
    """Function to parse graph and plot it"""

    # Make list of nodes ordered as in the graph
    nlist = list(graph.nodes)

    # Node positions
    pos = graph.graph["position"]

    node_size = []

    colour = []

    for node in graph.nodes():
        colour.append(graph.nodes[node]["distr"])

    nx.draw_networkx_nodes(
        graph, pos, node_color=colour, node_size=700, with_labels=True
    )
    nx.draw_networkx_edges(graph, pos, with_labels=True)
    nx.draw_networkx_labels(graph, pos)
    if fname:
        plt.savefig("imgs/{}.pdf".format(fname))


def colour_scale(colour="blue", all=None):
    """ Return dictionary of chosen colour scale. Setting all to true returns
    full colour palette of all four colours """

    # Define discrete colour scales
    scales = {
        "pink": {1: "#EE9BBB", 2: "#E26D9A", 3: "#CE477B", 4: "#BC2760", 5: "#951144"},
        "yellow": {
            1: "#FFDFA6",
            2: "#FFCF7B",
            3: "#EEB653",
            4: "#D99A2D",
            5: "#AC7514",
        },
        "blue": {1: "#91ABD4", 2: "#6081B6", 3: "#40649D", 4: "#285090", 5: "#173A72"},
        "green": {1: "#CCF39E", 2: "#B2EB71", 3: "#96D84B", 4: "#7CC528", 5: "#5C9C12"},
        "purple": {
            1: "#C6C7E1",
            2: "#ACAAD1",
            3: "#908DC2",
            4: "#796EB1",
            5: "#64479E",
        },
        "orange": {
            1: "#FCB97D",
            2: "#FD8C51",
            3: "#F87D2A",
            4: "#E95E0D",
            5: "#CC4401",
        },
    }
    if all:
        return scales
    else:
        for scale, _ in scales.items():
            if colour == scale:
                return scales[colour]


def single_plot_params(graph, stat, colour="blue", flat=False):
    """ Generate lists of key plotting parameters based off input graph and
    desired output statistic.  Colour argument accepts single colour scale of
    'pink', 'green', 'blue', or 'yellow'. Stat must be a statistic embedded in
    the graph, such as 'pop'. Returns lists of labels, sizes, and colors, in
    that order """

    # Create ordered node list
    nlist = list(graph.nodes)

    # List of values for the supplied statistic. Used to calculate discrete
    # boundaries between shades in colour scale
    stat_list = []

    # Colour palette and sizes definitions
    col_pal = colour_scale(colour)
    size_pal = {1: 10000, 2: 12000, 3: 14000, 4: 16000, 5: 18000}

    # Empty lists of main plot parameters to be populated
    col_map = []
    labels = {}
    sizes = []

    # Build quick list of statistic values
    for n in nlist:
        stat_list.append(graph.nodes[n][stat])
        labels[n] = graph.nodes[n][stat]
        if flat:
            col_map.append(col_pal[2])
            sizes.append(size_pal[4])

    # Deduce interval from statistic range
    intvl = int(round((max(stat_list) - min(stat_list)) / 5))

    intvls = {
        1: (min(stat_list) - 1, min(stat_list) + intvl),
        2: (min(stat_list) + intvl, min(stat_list) + 2 * intvl),
        3: (min(stat_list) + 2 * intvl, min(stat_list) + 3 * intvl),
        4: (min(stat_list) + 3 * intvl, min(stat_list) + 4 * intvl),
        5: (min(stat_list) + 4 * intvl, max(stat_list) + 1),
    }

    if not flat:
        for n in nlist:
            record = graph.nodes[n][stat]
            for i in range(1, 6):
                lower = intvls[i][0]
                upper = intvls[i][1]
                if lower <= record < upper:
                    col_map.append(col_pal[i])
                    sizes.append(size_pal[i])

    return labels, sizes, col_map


def distr_plot_params(graph, stat, colour="blue", flat=False):
    """ Generate lists of key plotting parameters based off input graph and
    desired output statistic.  Colour argument accepts single colour scale of
    'pink', 'green', 'blue', or 'yellow'. Stat must be a statistic embedded in
    the graph, such as 'pop'. Returns lists of labels, sizes, and colors, in
    that order """

    # Create ordered node list
    nlist = list(graph.nodes)

    # List of values for the supplied statistic. Used to calculate discrete
    # boundaries between shades in colour scale
    stat_list = []

    # Colour palette and sizes definitions
    col_pal = colour_scale(colour, all=True)
    col_names = [name for name, _ in col_pal.items()]
    size_pal = {1: 10000, 2: 12000, 3: 14000, 4: 16000, 5: 18000}

    # Empty lists of main plot parameters to be populated
    col_map = []
    labels = {}
    sizes = []

    # Build quick list of statistic values
    for n in nlist:
        stat_list.append(graph.nodes[n][stat])
        labels[n] = graph.nodes[n][stat]

    # Deduce interval from statistic range
    intvl = int(round((max(stat_list) - min(stat_list)) / 5))

    intvls = {
        1: (min(stat_list), min(stat_list) + intvl),
        2: (min(stat_list) + intvl + 1, min(stat_list) + 2 * intvl),
        3: (min(stat_list) + 2 * intvl + 1, min(stat_list) + 3 * intvl),
        4: (min(stat_list) + 3 * intvl + 1, min(stat_list) + 4 * intvl),
        5: (min(stat_list) + 4 * intvl + 1, max(stat_list)),
    }

    if flat:
        for n in nlist:
            record = graph.nodes[n][stat]
            distr = graph.nodes[n]["distr"]
            for j in range(1, 5):
                if distr == j:
                    col_map.append(col_pal[col_names[j - 1]][2])
                    sizes.append(size_pal[4])
    else:
        for n in nlist:
            record = graph.nodes[n][stat]
            distr = graph.nodes[n]["distr"]
            for j in range(1, 5):
                if distr == j:
                    for i in range(1, 6):
                        lower = intvls[i][0]
                        upper = intvls[i][1]
                        if lower <= record <= upper:
                            col_map.append(col_pal[col_names[j - 1]][i])
                            sizes.append(size_pal[i])

    return labels, sizes, col_map
