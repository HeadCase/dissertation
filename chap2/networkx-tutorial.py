"""
File: MCMC-example.py
Author: G. W. Headley
Email: mm19gwh@leeds.ac.uk
Github: https://github.com/HeadCase
Description: Python code to produce examples for dissertation chapter on
Markov chain Monte Carlo
"""

import networkx as nx

G = nx.Graph()

# Nodes can be created directly or from a list
G.add_node(1)
G.add_nodes_from([2, 3])

# Nested nodes can also be added from another graph
H = nx.path_graph(10)
G.add_nodes_from(H)

# We can add edges, directly, with attributes, from tuples, and from lists of
# tuples
G.add_edge(1, 2)
G.add_edge(3, 4, color="green")
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(4, 5), (5, 6)])

# We can extract details about the graph and manipulate the output into
# different containers
G.nodes
list(G.nodes)
set(G.nodes)
list(G.edges)
list(G.adj[3])  # get nodes adjacent to node 3
G.degree[2]  # the number of edges incident to 2

# Reports (edges and degree) of the graph can be queried using iterable of
# nodes
G.edges([2, 4])
G.degree([2, 4])

# We can remove nodes and edges just the way we added them
G.remove_node(7)
G.remove_edges_from([(1, 2), (4, 5)])

# In addition to Graph.edges() and Graph.adj(), we can 'index' to achieve the
# same results
G[3]  # same as G.adj[3]
G[3][4]  # same as G.edges[3, 4]

# We can also get/set edge attributes using the indexing function
G[3][4]["boundary"] = "water"
G[3][4]  # same as G.edges[3, 4]

# And similarly with nodes
G.nodes[3]["type"] = "county"

# As nodes and edges can have attributes, so can the entire graph
G.graph["state"] = "Testlandia"
G.graph["year"] = 2020
G.graph

# We can inspect the attributes of nodes and edges by querying their data
G.nodes.data()
G.edges.data()

# We can also create directed graphs
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
list(DG.predecessors(1))
list(DG.successors(1))


nx.draw(G, with_labels=True, node_size=800)
# nx.draw(DG, with_labels=True)
