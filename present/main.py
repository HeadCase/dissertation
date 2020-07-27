#!/usr/bin/env python
""" Main function """

# Imports
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from init import init_graph

# matplotlib.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
# matplotlib.rcParams["font.sans-serif"] = ["Tekton Pro"]
import matplotlib.font_manager as font_manager

# font_dirs = ["/Users/gheadley/CloudStation/home/docs/fonts/Adobe CC"]
# font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
# font_list = font_manager.createFontList(font_files)
# font_manager.fontManager.ttflist.extend(font_list)
# # mpl.rcParams["font.family"] = ["Source Sans"]
mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]

# font_manager._rebuild()


# import sys
# import numpy
# numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """
    S = init_graph()

    pos = S.graph["position"]
    nlist = list(S.nodes)
    sq_size = []
    cr_size = []
    sq_colour = []
    cr_colour = []
    fair_colour = []
    gerry_colour = []
    gerry_d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gerry_d2 = [10, 11, 12, 15, 16, 18, 24, 30, 36]
    gerry_d3 = [17, 22, 23, 28, 29, 32, 33, 34, 35]
    pink = {3: "#EE9BBB", 4: "#E26D9A", 5: "#CE477B", 6: "#BC2760", 7: "#951144"}
    yellow = {3: "#FFDFA6", 4: "#FFCF7B", 5: "#EEB653", 6: "#D99A2D", 7: "#AC7514"}
    blue = {3: "#91ABD4", 4: "#6081B6", 5: "#40649D", 6: "#285090", 7: "#173A72"}
    green = {3: "#CCF39E", 4: "#B2EB71", 5: "#96D84B", 6: "#7CC528", 7: "#5C9C12"}
    # gerry_d4 = [13, 14, 19, 20, 21, 25, 26, 27, 31]

    sqre_tot = 0
    for n in nlist:
        sq_size.append(S.nodes[n]["vote_sqre"] * 2000)
        sq_colour.append(S.nodes[n]["vote_sqre"])
        cr_size.append(S.nodes[n]["vote_circ"] * 2000)
        cr_colour.append(S.nodes[n]["vote_circ"])
        sqre_tot += S.nodes[n]["vote_sqre"]
        if S.nodes[n]["distr"] == 1:
            if S.nodes[n]["vote_sqre"] == 3:
                fair_colour.append(green[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                fair_colour.append(green[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                fair_colour.append(green[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                fair_colour.append(green[6])
            else:
                fair_colour.append(green[7])
        elif S.nodes[n]["distr"] == 2:
            if S.nodes[n]["vote_sqre"] == 3:
                fair_colour.append(yellow[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                fair_colour.append(yellow[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                fair_colour.append(yellow[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                fair_colour.append(yellow[6])
            else:
                fair_colour.append(yellow[7])
        elif S.nodes[n]["distr"] == 3:
            if S.nodes[n]["vote_sqre"] == 3:
                fair_colour.append(blue[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                fair_colour.append(blue[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                fair_colour.append(blue[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                fair_colour.append(blue[6])
            else:
                fair_colour.append(blue[7])
        else:
            if S.nodes[n]["vote_sqre"] == 3:
                fair_colour.append(pink[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                fair_colour.append(pink[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                fair_colour.append(pink[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                fair_colour.append(pink[6])
            else:
                fair_colour.append(pink[7])

    for n in nlist:
        if n in gerry_d1:
            if S.nodes[n]["vote_sqre"] == 3:
                gerry_colour.append(yellow[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                gerry_colour.append(yellow[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                gerry_colour.append(yellow[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                gerry_colour.append(yellow[6])
            else:
                gerry_colour.append(yellow[7])
        elif n in gerry_d2:
            if S.nodes[n]["vote_sqre"] == 3:
                gerry_colour.append(pink[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                gerry_colour.append(pink[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                gerry_colour.append(pink[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                gerry_colour.append(pink[6])
            else:
                gerry_colour.append(pink[7])
        elif n in gerry_d3:
            if S.nodes[n]["vote_sqre"] == 3:
                gerry_colour.append(green[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                gerry_colour.append(green[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                gerry_colour.append(green[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                gerry_colour.append(green[6])
            else:
                gerry_colour.append(green[7])
        else:
            if S.nodes[n]["vote_sqre"] == 3:
                gerry_colour.append(blue[3])
            elif S.nodes[n]["vote_sqre"] == 4:
                gerry_colour.append(blue[4])
            elif S.nodes[n]["vote_sqre"] == 5:
                gerry_colour.append(blue[5])
            elif S.nodes[n]["vote_sqre"] == 6:
                gerry_colour.append(blue[6])
            else:
                gerry_colour.append(blue[7])

    # dists = {
    #     1: [1, 2, 3, 7, 8, 9, 13, 14, 15],
    #     2: [4, 5, 6, 10, 11, 12, 16, 17, 18],
    #     3: [19, 20, 21, 25, 26, 27, 31, 32, 33],
    #     4: [22, 23, 24, 28, 29, 30, 34, 35, 36],

    # print(sqre_tot)

    sq_labels = {}
    cr_labels = {}
    labels = {}
    for index in range(len(nlist)):
        labels[nlist[index]] = "N:{} - {}".format(nlist[index], sq_colour[index])
        sq_labels[nlist[index]] = sq_colour[index]
        cr_labels[nlist[index]] = cr_colour[index]

    fig = plt.figure(figsize=[8, 6.5])  # , tight=True)  # , tight_layout=True)
    # fig, ax = plt.subplots()

    # fig.figsize = [8, 6.5]

    # Squares plot
    # nx.draw(
    #     S,
    #     pos,
    #     labels=sq_labels,
    #     font_size=72,
    #     node_list=nlist,
    #     node_size=sq_size,
    #     node_shape="s",
    #     node_color=sq_colour,
    #     vmin=0,
    #     vmax=9,
    #     linewidths=4,
    #     cmap=plt.cm.Purples,
    # )
    # plt.show()
    # plt.savefig("squares-baseline.pdf", bbox_inches="tight", pad_inches=3)

    # Circles plot
    nx.draw(
        S,
        pos,
        labels=cr_labels,
        font_size=72,
        node_list=nlist,
        node_size=cr_size,
        node_shape="o",
        node_color=cr_colour,
        vmin=0,
        vmax=9,
        linewidths=4,
        cmap=plt.cm.Oranges,
    )

    plt.show()

    # Fair Districting
    # nx.draw(
    #     S,
    #     pos,
    #     labels=sq_labels,
    #     font_size=52,
    #     node_list=nlist,
    #     node_size=sq_size,
    #     node_shape="s",
    #     node_color=fair_colour,
    #     vmin=0,
    #     vmax=9,
    #     linewidths=4,
    # )
    # plt.show()

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

    # nx.draw(
    #     S,
    #     pos,
    #     labels=labels,
    #     font_size=52,
    #     node_list=nlist,
    #     node_size=sq_size,
    #     node_shape="s",
    #     node_color=sq_colour,
    #     vmin=0,
    #     vmax=9,
    #     linewidths=4,
    #     cmap=plt.cm.Purples,
    # )
    # plt.show()

    # plt.savefig("circles-baseline.pdf", bbox_inches="tight", pad_inches=1)

    # fig.set_facecolor("#D0D0D0")


if __name__ == "__main__":
    main()
