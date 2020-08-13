#!/usr/bin/env python
""" Source code of utility functions used across the application """

from collections import deque


def distr_nodes(distr, graph):
    """ Accept a district from a graph and parse, producing a list of all
    nodes in that district """

    nodes_in_distr = [
        node for node, attrs in graph.nodes(data=True) if attrs["distr"] == distr
    ]

    return nodes_in_distr


def distr_count(graph):
    """ Function to retrieve the number of districts present in a supplied
    graph """

    distrs = []
    for _, values in graph.nodes.data():
        distrs.append(values["distr"])

    count = set(distrs)
    count = len(count)
    return count


def distr_pop(distr, graph):
    """ Tabulates the number of residents in a district """

    nodes_in_distr = distr_nodes(distr, graph)
    total_pop = 0
    for node in nodes_in_distr:
        total_pop += graph.nodes[node]["pop"]

    return total_pop


def contig_distr(distr, graph):
    """ Deploys breadth-first search algorithm to determine if supplied
    district is contiguous. Returns boolean result """

    # Produce list of nodes in the district in question
    d_nodes = distr_nodes(distr, graph)

    # A proposal plan which eliminates a district will get rejected 100% of the
    # time due to transition probabilities, but this function is called first.
    # Hence we return false if a district has no nodes
    if not d_nodes:
        return False
    else:
        init_node = d_nodes[0]

        # Send required arguments to breadth-first search (BFS) algorithm to
        # get a list of contiguous nodes in the district
        contig_nodes = bfs(init_node, graph)

        # While the code above initialises with the first node in the district, it
        # doesn't really matter. If the BFS returns any list of contiguous nodes
        # that is not exactly the same as the full list of nodes in the district,
        # the district cannot be contiguous
        if set(d_nodes) == set(contig_nodes):
            return True
        else:
            return False


def bfs(node, graph):
    """ Breadth-first search (BFS) for traversing the full set of nodes, from
    the supplied district, which are contiguous. """

    # BFS is implemented using a queue and visit pair of lists. The queue
    # tracks nodes that need to be explored. Once explored, they are removed
    # from the queue and appended to the visited list. A while loop keeps the
    # search going until the queue is empty.
    queue = deque([node])
    visited = [node]

    # Get district of supplied node
    distr = graph.nodes[node]["distr"]

    while queue:
        curr_node = queue.popleft()
        nbors = list(graph.neighbors(curr_node))
        d_nbors = [item for item in nbors if graph.nodes[item]["distr"] == distr]
        for n in d_nbors:
            if n not in visited:
                queue.append(n)
                visited.append(n)

    return visited
