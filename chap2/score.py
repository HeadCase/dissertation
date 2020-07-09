#!/usr/bin/env python
""" Source code for scoring districting plans """


def score_plan(plan):
    """ Accepts a districting plan in the form of a networkx graph and scores
    it for apportionment equality. The score function is a simple sum of
    squares calculation on population values for each district in the state.
    """

    # plans list, containing a series of graphs of possible
    # districting plans, and rejects any plans where the population of any
    # district exceeds: total population * 1/number of districts (+/- 10%).
    # Returns a list of plans with non-contiguous plans removed"""

    # Retrieve the number of districts in the given plan and create empty list
    # for population values from each district
    num_distrs = distr_count(graph)
    distr_pops = []

    # For each district in the plan, retrieve the nodes of that district
    # and test each node to confirm that at least one of its neighbors is
    # from the same district
    for i in range(1, num_distrs + 1):
        # Create empty list to be populated with booleans for each node in
        # the current district
        distr_check = True

        nodes_in_distr = [
            node for node, attrs in graph.nodes(data=True) if attrs["distr"] == i
        ]
        total_pop = 0
        for node in nodes_in_distr:
            total_pop += graph.nodes[node]["pop"]

        if total_pop > 255 or total_pop < 245:
            distr_check = False

        graph_check.append(distr_check)

    if False in graph_check:
        reject_plans.append(graph)
    else:
        clean_plans.append(graph)

    return clean_plans, reject_plans
