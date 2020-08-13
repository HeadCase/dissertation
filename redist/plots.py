#!/usr/bin/env python
""" Main function """

# Imports
from init import init_graph
from draw import single_plot_params
from draw import distr_plot_params

import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

import matplotlib.font_manager as font_manager

mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]


def main():
    """ Main function """

    # col_map = colour_scale(all=True)
    # print(col_map[1])
    S = init_graph()
    labs, sizes, colours = distr_plot_params(S, "node label", "purple", flat=True)
    # print(len(labs), len(sizes), len(colours))
    pos = S.graph["position"]
    nlist = list(S.nodes)
    # colours = [marg[1] for marg in S.nodes.data("sqre_marg")]

    nx.draw(
        S,
        pos,
        labels=labs,
        node_list=nlist,
        node_color=colours,
        node_size=sizes,
        font_size=56,
        node_shape="o",
        # cmap=plt.cm.RdYlGn,
    )
    plt.show()


if __name__ == "__main__":
    main()
