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


def colour_scale(colour, all=None):
    """ Return dictionary of chosen colour scale """

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
    }
    if all:
        return scales
    else:
        for scale, _ in scales.items():
            if colour == scale:
                return scales[colour]


def single_plot_params(graph, stat, colour="blue"):
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

    # Deduce interval from statistic range
    intvl = int(round((max(stat_list) - min(stat_list)) / 5))

    intvls = {
        1: (min(stat_list), min(stat_list) + intvl),
        2: (min(stat_list) + intvl + 1, min(stat_list) + 2 * intvl),
        3: (min(stat_list) + 2 * intvl + 1, min(stat_list) + 3 * intvl),
        4: (min(stat_list) + 3 * intvl + 1, min(stat_list) + 4 * intvl),
        5: (min(stat_list) + 4 * intvl + 1, max(stat_list)),
    }

    for n in nlist:
        record = graph.nodes[n][stat]
        for i in range(1, 6):
            lower = intvls[i][0]
            upper = intvls[i][1]
            if lower <= record <= upper:
                col_map.append(col_pal[i])
                sizes.append(size_pal[i])

    return labels, sizes, col_map


def distr_plot_params(graph, stat, colour="blue"):
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

    # Deduce interval from statistic range
    intvl = int(round((max(stat_list) - min(stat_list)) / 5))

    intvls = {
        1: (min(stat_list), min(stat_list) + intvl),
        2: (min(stat_list) + intvl + 1, min(stat_list) + 2 * intvl),
        3: (min(stat_list) + 2 * intvl + 1, min(stat_list) + 3 * intvl),
        4: (min(stat_list) + 3 * intvl + 1, min(stat_list) + 4 * intvl),
        5: (min(stat_list) + 4 * intvl + 1, max(stat_list)),
    }

    for n in nlist:
        record = graph.nodes[n][stat]
        for i in range(1, 6):
            lower = intvls[i][0]
            upper = intvls[i][1]
            if lower <= record <= upper:
                col_map.append(col_pal[i])
                sizes.append(size_pal[i])

    return labels, sizes, col_map

    # for n in nlist:
    #     if S.nodes[n]["distr"] == 1:
    #         if S.nodes[n]["vote_sqre"] == 3:
    #             fair_colour.append(green[3])
    #         elif S.nodes[n]["vote_sqre"] == 4:
    #             fair_colour.append(green[4])
    #         elif S.nodes[n]["vote_sqre"] == 5:
    #             fair_colour.append(green[5])
    #         elif S.nodes[n]["vote_sqre"] == 6:
    #             fair_colour.append(green[6])
    #         else:
    #             fair_colour.append(green[7])
    #     elif S.nodes[n]["distr"] == 2:
    #         if S.nodes[n]["vote_sqre"] == 3:
    #             fair_colour.append(yellow[3])
    #         elif S.nodes[n]["vote_sqre"] == 4:
    #             fair_colour.append(yellow[4])
    #         elif S.nodes[n]["vote_sqre"] == 5:
    #             fair_colour.append(yellow[5])
    #         elif S.nodes[n]["vote_sqre"] == 6:
    #             fair_colour.append(yellow[6])
    #         else:
    #             fair_colour.append(yellow[7])
    #     elif S.nodes[n]["distr"] == 3:
    #         if S.nodes[n]["vote_sqre"] == 3:
    #             fair_colour.append(blue[3])
    #         elif S.nodes[n]["vote_sqre"] == 4:
    #             fair_colour.append(blue[4])
    #         elif S.nodes[n]["vote_sqre"] == 5:
    #             fair_colour.append(blue[5])
    #         elif S.nodes[n]["vote_sqre"] == 6:
    #             fair_colour.append(blue[6])
    #         else:
    #             fair_colour.append(blue[7])
    #     else:
    #         if S.nodes[n]["vote_sqre"] == 3:
    #             fair_colour.append(pink[3])
    #         elif S.nodes[n]["vote_sqre"] == 4:
    #             fair_colour.append(pink[4])
    #         elif S.nodes[n]["vote_sqre"] == 5:
    #             fair_colour.append(pink[5])
    #         elif S.nodes[n]["vote_sqre"] == 6:
    #             fair_colour.append(pink[6])
    #         else:
    #             fair_colour.append(pink[7])


# def colours_distr(graph,):
#     """or 'multi' for all four in one plot. If multi is used, it is assumed that
#     colours are to be split by district, and the supplied statistic breaks down
#     within each district  """
#     pass


# def sizes_lists():
#     pass


# def labels_lists():
#     pass


# def main():
#     """ Main function """
#     S = init_graph()

#     sq_size = []
#     cr_size = []
#     sq_colour = []
#     cr_colour = []
#     fair_colour = []
#     gerry_colour = []
#     gerry_d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     gerry_d2 = [10, 11, 12, 15, 16, 18, 24, 30, 36]
#     gerry_d3 = [17, 22, 23, 28, 29, 32, 33, 34, 35]
#     pink = {3: "#EE9BBB", 4: "#E26D9A", 5: "#CE477B", 6: "#BC2760", 7: "#951144"}
#     yellow = {3: "#FFDFA6", 4: "#FFCF7B", 5: "#EEB653", 6: "#D99A2D", 7: "#AC7514"}
#     blue = {3: "#91ABD4", 4: "#6081B6", 5: "#40649D", 6: "#285090", 7: "#173A72"}
#     green = {3: "#CCF39E", 4: "#B2EB71", 5: "#96D84B", 6: "#7CC528", 7: "#5C9C12"}
#     # gerry_d4 = [13, 14, 19, 20, 21, 25, 26, 27, 31]

#     sqre_tot = 0
#     for n in nlist:
#         sq_size.append(S.nodes[n]["vote_sqre"] * 2000)
#         sq_colour.append(S.nodes[n]["vote_sqre"])
#         cr_size.append(S.nodes[n]["vote_circ"] * 2000)
#         cr_colour.append(S.nodes[n]["vote_circ"])
#         sqre_tot += S.nodes[n]["vote_sqre"]
#         if S.nodes[n]["distr"] == 1:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 fair_colour.append(green[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 fair_colour.append(green[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 fair_colour.append(green[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 fair_colour.append(green[6])
#             else:
#                 fair_colour.append(green[7])
#         elif S.nodes[n]["distr"] == 2:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 fair_colour.append(yellow[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 fair_colour.append(yellow[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 fair_colour.append(yellow[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 fair_colour.append(yellow[6])
#             else:
#                 fair_colour.append(yellow[7])
#         elif S.nodes[n]["distr"] == 3:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 fair_colour.append(blue[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 fair_colour.append(blue[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 fair_colour.append(blue[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 fair_colour.append(blue[6])
#             else:
#                 fair_colour.append(blue[7])
#         else:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 fair_colour.append(pink[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 fair_colour.append(pink[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 fair_colour.append(pink[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 fair_colour.append(pink[6])
#             else:
#                 fair_colour.append(pink[7])

#     for n in nlist:
#         if n in gerry_d1:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 gerry_colour.append(yellow[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 gerry_colour.append(yellow[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 gerry_colour.append(yellow[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 gerry_colour.append(yellow[6])
#             else:
#                 gerry_colour.append(yellow[7])
#         elif n in gerry_d2:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 gerry_colour.append(pink[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 gerry_colour.append(pink[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 gerry_colour.append(pink[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 gerry_colour.append(pink[6])
#             else:
#                 gerry_colour.append(pink[7])
#         elif n in gerry_d3:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 gerry_colour.append(green[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 gerry_colour.append(green[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 gerry_colour.append(green[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 gerry_colour.append(green[6])
#             else:
#                 gerry_colour.append(green[7])
#         else:
#             if S.nodes[n]["vote_sqre"] == 3:
#                 gerry_colour.append(blue[3])
#             elif S.nodes[n]["vote_sqre"] == 4:
#                 gerry_colour.append(blue[4])
#             elif S.nodes[n]["vote_sqre"] == 5:
#                 gerry_colour.append(blue[5])
#             elif S.nodes[n]["vote_sqre"] == 6:
#                 gerry_colour.append(blue[6])
#             else:
#                 gerry_colour.append(blue[7])

# dists = {
#     1: [1, 2, 3, 7, 8, 9, 13, 14, 15],
#     2: [4, 5, 6, 10, 11, 12, 16, 17, 18],
#     3: [19, 20, 21, 25, 26, 27, 31, 32, 33],
#     4: [22, 23, 24, 28, 29, 30, 34, 35, 36],

# print(sqre_tot)

# sq_labels = {}
# cr_labels = {}
# labels = {}
# for index in range(len(nlist)):
#     labels[nlist[index]] = "N:{} - {}".format(nlist[index], sq_colour[index])
#     sq_labels[nlist[index]] = sq_colour[index]
#     cr_labels[nlist[index]] = cr_colour[index]

# fig = plt.figure(figsize=[8, 6.5])  # , tight=True)  # , tight_layout=True)
# fig, ax = plt.subplots()

# fig.figsize = [8, 6.5]

# Gerrymandered Districting
# nx.draw(
#     S,
#     pos,
#     labels=sq_labels,
#     font_size=52,
#     node_list=nlist,
#     node_size=sq_size,
#     node_shape="s",
#     node_color=gerry_colour,
#     vmin=0,
#     vmax=9,
#     linewidths=4,
# )
# plt.show()
