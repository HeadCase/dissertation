#!/usr/bin/env python
""" Main function """

# Imports
from init import init_expanded
from draw import single_plot_params
from draw import distr_plot_params
from draw import remappedColorMap

import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

# import matplotlib.font_manager as font_manager

mpl.rcParams["font.family"] = ["sans-serif"]  # fancy fonts
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]


def main():
    """ Main function """

    # # col_map = colour_scale(all=True)
    # # print(col_map[1])
    # # S = init_graph()
    # S = init_expanded()
    # # labs, sizes, colours = single_plot_params(S, "pop", "blue", flat=False)
    # labs, sizes, colours = distr_plot_params(S, "pop", "purple", flat=False)
    # # print(len(labs), len(sizes), len(colours))
    # pos = S.graph["position"]
    # nlist = list(S.nodes)
    # # colours = [marg[1] for marg in S.nodes.data("circ_marg")]
    # # colours = [marg[1] for marg in S.nodes.data("sqre_marg")]

    # nx.draw(
    #     S,
    #     pos,
    #     labels=labs,
    #     node_list=nlist,
    #     node_color=colours,
    #     node_size=sizes,
    #     font_size=40,
    #     node_shape="o",
    #     # cmap=plt.cm.RdYlGn,
    # )
    # plt.show()

    # Special sauce for heatmaps to get the colour scale zero-centred. For
    # circle margins, need to define end but leave start at default, vice-versa
    # for square margin
    S = init_expanded()
    labs, sizes, colours = single_plot_params(S, "circ_marg", "blue", flat=False)
    pos = S.graph["position"]
    nlist = list(S.nodes)
    # marg is a dict, so first index is the margin value for the given node
    colours = [marg[1] for marg in S.nodes.data("circ_marg")]
    # colours = [marg[1] for marg in S.nodes.data("sqre_marg")]

    vmin = min(colours)
    vmax = max(colours)
    mpoint = abs(vmin) / (vmax + abs(vmin))

    rdylgn = plt.cm.RdYlGn
    heat_cmap = remappedColorMap(rdylgn, midpoint=mpoint)

    nx.draw(
        S,
        pos,
        labels=labs,
        node_list=nlist,
        node_color=colours,
        node_size=8000,
        font_size=40,
        node_shape="o",
        cmap=heat_cmap,
    )
    plt.show()


if __name__ == "__main__":
    main()

# def remappedColorMap(cmap, start=0, midpoint=0.5, stop=1.0, name="shiftedcmap"):
#     """
#     Function to offset the median value of a colormap, and scale the
#     remaining color range. Useful for data with a negative minimum and
#     positive maximum where you want the middle of the colormap's dynamic
#     range to be at zero.
#     Input
#     -----
#       cmap : The matplotlib colormap to be altered
#       start : Offset from lowest point in the colormap's range.
#           Defaults to 0.0 (no lower ofset). Should be between
#           0.0 and 0.5; if your dataset mean is negative you should leave
#           this at 0.0, otherwise to (vmax-abs(vmin))/(2*vmax)
#       midpoint : The new center of the colormap. Defaults to
#           0.5 (no shift). Should be between 0.0 and 1.0; usually the
#           optimal value is abs(vmin)/(vmax+abs(vmin))
#       stop : Offset from highets point in the colormap's range.
#           Defaults to 1.0 (no upper ofset). Should be between
#           0.5 and 1.0; if your dataset mean is positive you should leave
#           this at 1.0, otherwise to (abs(vmin)-vmax)/(2*abs(vmin))
#     """
