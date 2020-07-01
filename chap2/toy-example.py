#!/usr/bin/env python
"""
File: toy-example.py
Author: G. W. Headley
Email: mm19gwh@leeds.ac.uk
Github: https://github.com/HeadCase
Description: Source code for example MCMC/redistricting example in
introductory MCMC chapter
"""

import networkx as nx
import pandas as pd

vtds = [
    "VTD1",
    "VTD2",
    "VTD3",
    "VTD4",
    "VTD5",
    "VTD6",
    "VTD7",
    "VTD8",
    "VTD9",
    "VTD10",
    "VTD11",
    "VTD12",
    "VTD13",
    "VTD14",
    "VTD15",
    "VTD16",
    "VTD17",
    "VTD18",
    "VTD19",
    "VTD20",
    "VTD21",
    "VTD22",
    "VTD23",
    "VTD24",
    "VTD25",
    "VTD26",
    "VTD27",
    "VTD28",
    "VTD29",
    "VTD30",
    "VTD31",
    "VTD32",
    "VTD33",
    "VTD34",
    "VTD35",
    "VTD36",
]

dists = [
    4,
    4,
    4,
    4,
    5,
    5,
    5,
    6,
    6,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
]

edges = [
    ("VTD36", "VTD18"),
    "VTD1",
    "VTD2",
    "VTD3",
    "VTD4",
    "VTD5",
    "VTD6",
    "VTD7",
    "VTD8",
    "VTD9",
    "VTD10",
    "VTD11",
    "VTD12",
    "VTD13",
    "VTD14",
    "VTD15",
    "VTD16",
    "VTD17",
    "VTD18",
    "VTD19",
    "VTD20",
    "VTD21",
    "VTD22",
    "VTD23",
    "VTD24",
    "VTD25",
    "VTD26",
    "VTD27",
    "VTD28",
    "VTD29",
    "VTD30",
    "VTD31",
    "VTD32",
    "VTD33",
    "VTD34",
    "VTD35",
]


df = pd.DataFrame(columns=["VTDs", "Districts", "Edges"])
df["VTDs"] = vtds
df["Districts"] = dists
df["Edges"] = edges

# df.head()

G = nx.from_pandas_edgelist(df, "VTDs", "Edges")

# G = nx.Graph(state="Toylandia")

# nodes = list(range(1, 50))

# G.add_nodes_from(nodes)

nx.draw(G, with_labels=True)


df2 = pd.DataFrame([[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
df2
G = nx.from_pandas_adjacency(df2)
nx.draw(G, with_labels=True, node_shape="s")
print(nx.info(G))
