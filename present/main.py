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
import matplotlib.font_manager as font_manager
mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]

# font_manager._rebuild()


# import sys
# import numpy
# numpy.set_printoptions(threshold=sys.maxsize)


def main():
    """ Main function """
    S = init_graph()

    # S.nodes[21]["distr"] = 1

    pos = S.graph["position"]
    nlist = list(S.nodes)
    size = []
    colour = []

    for n in nlist:
        size.append((S.nodes[n]["pop"] ** 3) / 3)
        if S.nodes[n]["distr"] == 1:
            colour.append("#EEB653")
        elif S.nodes[n]["distr"] == 2:
            colour.append("#CE477B")
        elif S.nodes[n]["distr"] == 3:
            colour.append("#40649D")
        else:
            colour.append("#96D84B")

    labels = {}
    for n in nlist:
        labels[n] = S.nodes[n]["pop"]

    nx.draw(
        S,
        pos,
        labels=labels,
        font_size=60,
        node_list=nlist,
        node_size=size,
        node_shape="s",
        node_color=colour,
        linewidths=4,
        width=4,
    )
    plt.show()


if __name__ == "__main__":
    main()
