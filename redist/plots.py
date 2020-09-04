#!/usr/bin/env python
""" Main function """

# Imports
from init import init_expanded
from init import gerry
from log import from_json
from utils import distr_pop
from utils import distr_count
from utils import remove_dups
from draw import single_plot_params
from draw import distr_plot_params
from draw import remappedColorMap

from statistics import pstdev
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

# Fancy font stuff
mpl.rcParams["font.family"] = ["sans-serif"]
mpl.rcParams["font.sans-serif"] = ["Source Sans Pro"]


def main():
    """ Main function """

    # prod_run = from_json(
    #     "plans/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1.json"
    # )
    # gerry_plans = [
    #     276,
    #     310,
    #     392,
    #     401,
    #     454,
    #     463,
    #     499,
    #     567,
    #     692,
    #     710,
    #     716,
    #     717,
    #     920,
    #     1145,
    # ]

    # count = 0
    # for plan in prod_run:
    #     if count in gerry_plans:
    #         labs, sizes, colours = distr_plot_params(plan, "distr", "blue", flat=True)
    #         pos = plan.graph["position"]
    #         nlist = list(plan.nodes)

    #         plt.figure(figsize=(19, 15))
    #         nx.draw(
    #             plan,
    #             pos,
    #             labels=labs,
    #             node_list=nlist,
    #             node_color=colours,
    #             node_size=sizes,
    #             font_size=40,
    #             node_shape="o",
    #             # cmap=plt.cm.RdYlGn,
    #         )
    #         plt.show()
    #     count += 1

    S = init_expanded()

    labs, sizes, colours = single_plot_params(S, "pop", "blue")
    # labs, sizes, colours = distr_plot_params(S, "node label", "blue")
    pos = S.graph["position"]
    nlist = list(S.nodes)

    plt.figure(figsize=(19, 15))
    nx.draw(
        S,
        pos,
        labels=labs,
        node_list=nlist,
        node_color=colours,
        node_size=sizes,
        font_size=40,
        node_shape="o",
        # cmap=plt.cm.RdYlGn,
    )
    plt.show()

    # S = gerry(S)

    # labs, sizes, colours = distr_plot_params(S, "distr", "blue", flat=True)
    # pos = S.graph["position"]
    # nlist = list(S.nodes)

    # plt.figure(figsize=(19, 15))
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

    # plans = from_json("plans/1000000-iters-exp-graph-working-params.json")
    # uniq_lgl_plans = remove_dups(plans)

    # count = 1
    # for plan in uniq_lgl_plans:
    #     distr_pops = []
    #     dcnt = distr_count(plan)
    #     for distr in range(1, dcnt + 1):
    #         distr_pops.append(distr_pop(distr, plan))
    #     if 0 < pstdev(distr_pops) <= 5:
    #         print(
    #             "Plan {} districts have population: {} (std dev:{})".format(
    #                 1 + uniq_lgl_plans.index(plan),
    #                 distr_pops,
    #                 round(pstdev(distr_pops), 1),
    #             )
    #         )
    #         labs, sizes, colours = distr_plot_params(plan, "pop", "blue")
    #         pos = plan.graph["position"]
    #         nlist = list(plan.nodes)

    #         plt.figure(figsize=(19, 15))
    #         nx.draw(
    #             plan,
    #             pos,
    #             labels=labs,
    #             node_list=nlist,
    #             node_color=colours,
    #             node_size=sizes,
    #             font_size=40,
    #             node_shape="o",
    #             # cmap=plt.cm.RdYlGn,
    #         )
    #         # plt.show()
    #         plt.savefig("imgs/1mil-exp-graph-under5-stdev-{}.pdf".format(count))
    #         count += 1

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
    # S = init_expanded()
    # labs, sizes, colours = single_plot_params(S, "circ_marg", "blue", flat=False)
    # pos = S.graph["position"]
    # nlist = list(S.nodes)
    # # marg is a dict, so first index is the margin value for the given node
    # colours = [marg[1] for marg in S.nodes.data("circ_marg")]
    # # colours = [marg[1] for marg in S.nodes.data("sqre_marg")]

    # vmin = min(colours)
    # vmax = max(colours)
    # # start = (vmax - abs(vmin)) / (4 * vmax)
    # # stop = (abs(vmin) - vmax) / (4 * vmin)
    # mpoint = abs(vmin) / (vmax + abs(vmin))

    # rdylgn = plt.cm.RdYlGn
    # heat_cmap = remappedColorMap(rdylgn, midpoint=mpoint)

    # nx.draw(
    #     S,
    #     pos,
    #     labels=labs,
    #     node_list=nlist,
    #     node_color=colours,
    #     node_size=sizes,
    #     font_size=32,
    #     node_shape="o",
    #     cmap=heat_cmap,
    # )
    # plt.show()


if __name__ == "__main__":
    main()
