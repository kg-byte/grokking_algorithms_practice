# Recap
# Breadth-first search is used to calculate the shortest path for an unweighted graph.
# Dijkstra's algorithm is used to calculate the shortest path for a weighted graph.
# Dijkstra's algorithm works well when all weights are positive.
# If you have negative weights, use the Bellman-Ford algorithm.


INFINITY = float("inf")
COSTS = dict[str, int | float]
GRAPH = dict[str, dict[str, int]]
PARENTS = dict[str, str | None]


# keep track of processed

# while nodes to process ->
# grab the node that is closest to start ->
# update costs for its neighbors ->
# if neighbor's cost is updated, update paretn too ->
# mark this node processed


def diakstras_algorithm(costs: COSTS, graph: GRAPH, parents: PARENTS, fin: str):
    # find lowest cost node to start
    processed: list[str] = []

    def find_lowest_cost_node(costs: dict[str, int | float]) -> str | None:
        lowest_cost = INFINITY
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            # find the lowest cost in costs hash that's unprocessed; ignore processed
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        # find neighbors of node
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # update neighbors costs if new_cost is lower
            # if costs updated, udpate parent to current node
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        # add to processed node once all neighbors processed
        processed.append(node)
        # find next lowest cost node until no node is left(unprocessed)
        node = find_lowest_cost_node(costs)
    # return target
    return costs[fin]


def main():
    # graph hash to describe graph
    # start-6->a
    # start-2->b
    # b-3->a
    # b-5->fin
    # a-1->fin
    graph: GRAPH = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    # costs table to store costs for each node
    costs: dict[str, int | float] = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = INFINITY

    # parents table to store parents
    parents: dict[str, str | None] = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    assert diakstras_algorithm(costs, graph, parents, "fin") == 6

    # exercise 1
    # graph
    graph_1: GRAPH = {}
    graph_1["start"] = {}
    graph_1["start"]["a"] = 5
    graph_1["start"]["b"] = 2
    graph_1["a"] = {}
    graph_1["a"]["c"] = 4
    graph_1["a"]["d"] = 2
    graph_1["b"] = {}
    graph_1["b"]["a"] = 8
    graph_1["b"]["d"] = 7
    graph_1["c"] = {}
    graph_1["c"]["fin"] = 3
    graph_1["c"]["d"] = 6
    graph_1["d"] = {}
    graph_1["d"]["fin"] = 1
    graph_1["fin"] = {}

    # costs
    costs_1: COSTS = {}
    costs_1["a"] = 5
    costs_1["b"] = 2
    costs_1["c"] = INFINITY
    costs_1["d"] = INFINITY
    costs_1["fin"] = INFINITY

    # parents
    parents_1: PARENTS = {}
    parents_1["a"] = "start"
    parents_1["b"] = "start"
    parents_1["c"] = None
    parents_1["d"] = None
    parents_1["fin"] = None
    assert diakstras_algorithm(costs_1, graph_1, parents_1, "fin") == 8

    # exercise 2
    # graph
    graph_2: GRAPH = {}
    graph_2["start"] = {}
    graph_2["start"]["a"] = 10
    graph_2["a"] = {}
    graph_2["a"]["c"] = 20
    graph_2["b"] = {}
    graph_2["b"]["a"] = 1
    graph_2["c"] = {}
    graph_2["c"]["fin"] = 30
    graph_2["c"]["b"] = 1
    graph_2["fin"] = {}

    # costs
    costs_2: COSTS = {}
    costs_2["a"] = 10
    costs_2["b"] = 31
    costs_2["c"] = 30
    costs_2["fin"] = INFINITY

    # parents
    parents_2: PARENTS = {}
    parents_2["a"] = "start"
    parents_2["b"] = "start"
    parents_2["c"] = None
    parents_2["d"] = None
    parents_2["fin"] = None
    assert diakstras_algorithm(costs_2, graph_2, parents_2, "fin") == 60


if __name__ == "__main__":
    main()
