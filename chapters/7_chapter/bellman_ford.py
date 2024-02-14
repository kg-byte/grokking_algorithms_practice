from dataclasses import dataclass, field


@dataclass
class Edge:
    start: str
    end: str
    weight: int


@dataclass
class Graph:
    vertices: list[str]
    graph: list[Edge] = field(default_factory=list)

    def add_edge(self, edge: Edge):
        self.graph.append(edge)

    def print_solution(self, distance: dict[str, int | float], source: str):
        print(f"Vertex          Distance from Source {source}")

        for k in self.vertices:
            print("{0}\t\t{1}".format(k, distance[k]))

    def bellman_ford(self, source: str):
        distances: dict[str, float | int] = {}
        for v in self.vertices:
            distances[v] = float("Inf")
        distances[source] = 0

        for _ in range(len(self.vertices) - 1):
            for edge in self.graph:
                if (
                    distances[edge.start] != float("Inf")
                    and distances[edge.start] + edge.weight < distances[edge.end]
                ):
                    distances[edge.end] = distances[edge.start] + edge.weight

        for edge in self.graph:
            if (
                distances[edge.start] != float("Inf")
                and distances[edge.start] + edge.weight < distances[edge.end]
            ):
                print("Graph contains negative weight cycle")
                return

        self.print_solution(distances, source)


g = Graph(["P", "Q", "R", "S", "T"])
g.add_edge(Edge("P", "Q", 2))
g.add_edge(Edge("P", "R", 4))
g.add_edge(Edge("Q", "S", 2))
g.add_edge(Edge("R", "T", 3))
g.add_edge(Edge("R", "S", 4))
g.add_edge(Edge("T", "S", -5))

g.bellman_ford("P")


g = Graph(["P", "Q", "R", "S", "T"])
g.add_edge(Edge("P", "Q", 2))
g.add_edge(Edge("P", "R", 4))
g.add_edge(Edge("Q", "S", 2))
g.add_edge(Edge("R", "T", 3))
g.add_edge(Edge("R", "S", 4))
g.add_edge(Edge("T", "S", -5))

g.bellman_ford("P")
