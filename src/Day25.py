from utilities.get_input import *
from utilities.parse import *
import time, math
import networkx as nx
from progress.bar import Bar
from collections import defaultdict


class Day25:
    def __init__(self) -> None:
        self.input = get_input(2023, 25)
        self.parsed_input = parse_lines(self.input)
        self.component_graph = self.parse_components()
        return

    def parse_components(self) -> nx.Graph:
        component_graph = nx.Graph()
        for line in self.parsed_input:
            input, outputs = line.split(": ")
            for component in outputs.split(" "):
                component_graph.add_edge(input, component)
        return component_graph

    def solve(self) -> None:
        start_time = time.time()
        edge_frequency = defaultdict(int)
        nodes = [*self.component_graph.nodes]
        bar = Bar("Processing", max=len(nodes))
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                path = nx.shortest_path(self.component_graph, nodes[i], nodes[j])
                for k in range(len(path) - 1):
                    edge = (
                        (path[k], path[k + 1])
                        if path[k] < path[k + 1]
                        else (path[k + 1], path[k])
                    )
                    edge_frequency[edge] += 1
            bar.next()
        bar.finish()
        # Remove the 3 paths which have been used the most
        for _ in range(3):
            max_edge = max(edge_frequency, key=edge_frequency.get)
            self.component_graph.remove_edge(*max_edge)
            del edge_frequency[max_edge]
        size_of_subgraphs = [
            len(self.component_graph.subgraph(node))
            for node in nx.connected_components(self.component_graph)
        ]
        output = math.prod(size_of_subgraphs)
        print(f"Part 1: {output} - {time.time() - start_time}")


def main() -> None:
    day = Day25()
    day.solve()
    return


if __name__ == "__main__":
    main()
