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
G.add_node(1)
G.add_nodes_from([2, 3])

nx.draw(G)
