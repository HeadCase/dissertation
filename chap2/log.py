#!/usr/bin/env python
""" Functions for producing logs of chain runs and results and loading them
back up """

from networkx.readwrite import json_graph
import json


def to_json(list, fname):
    """ Accepts a list of networkx graphs and dumps them to file for later
    reading """

    count = 1
    master = {}
    for plan in list:
        data = json_graph.adjacency_data(plan)
        master["graph-{}".format(count)] = data
        count += 1

    with open("{}.json".format(fname), "w") as f:
        json.dump(master, f, indent=2)


def from_json(fname):
    """ Load json file of graph(s) and stuff them into a list of networkx
    graphs"""

    with open("{}.json".format(fname)) as f:
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
