#!/usr/bin/env python
""" Functions for reading and writing networkx graphs to JSON files for logging
purposes """

import json
from networkx.readwrite import json_graph


def to_json(glist, fname):
    """ Accepts a list of networkx graphs and dumps them to file for later
    reading """

    count = 1
    master = {}
    for plan in glist:
        data = json_graph.adjacency_data(plan)
        master["graph-{}".format(count)] = data
        count += 1

    with open("{}".format(fname), "w") as f:
        json.dump(master, f, indent=2)


def from_json(fname):
    """ Load json file of graph(s) and stuff them into a list of networkx
    graphs """

    with open("{}".format(fname)) as f:
        master = json.load(f)

    graphs = []
    for key, value in master.items():
        data = json_graph.adjacency_graph(value, multigraph=False)

        # JSON dump does funny business with the position dictionary, changing
        # the tuples to lists and ints to string. This reverses the screwy API
        data.graph["position"] = {
            int(key): tuple(value) for key, value in data.graph["position"].items()
        }

        graphs.append(data)

    return graphs
