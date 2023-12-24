from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from enum import Enum
import networkx as nx

type Position = tuple[int, int]
type Hike = set[Position]

class Direction(Enum):
    RIGHT = (1,  0)
    LEFT =  (-1, 0)
    UP =    (0, -1)
    DOWN =  (0,  1)

class Day23:
    def __init__(self) -> None:
        self.input = get_input(2023, 23)
        self.maze = Grid(self.input)
        self.start_position = (1, 0)
        self.end_position = (self.maze.max_x - 1, self.maze.max_y)
        return
    
    def find_intersection(self, position: Position, hike: Hike, part_2: bool) -> Position:
        for direction in Direction:
            new_position = (position[0] + direction.value[0], position[1] + direction.value[1])
            if new_position in hike:
                continue # We have already been here
            if new_position == self.end_position or new_position == self.start_position:
                hike.add(new_position) # End or start reached, we are done
                return new_position
            symbol = self.maze.get(*new_position)
            if symbol == None or symbol == '#':
                continue # We can not go here
            if symbol == '.':
                hike.add(new_position)
                return self.find_intersection(new_position, hike, part_2)
            elif symbol == '>' or symbol == '<' or symbol == '^' or symbol == 'v':
                hike.add(new_position)
                intersection = (new_position[0] + direction.value[0], new_position[1] + direction.value[1])
                hike.add(intersection)
                return intersection
            
    def branch(self, position: Position, graph: nx.DiGraph, part_2: bool) -> None:
        for direction in Direction:
            hike: Hike = {position}
            new_position = (position[0] + direction.value[0], position[1] + direction.value[1])
            symbol = self.maze.get(*new_position)
            if symbol == None or symbol == '#':
                continue # We can not go here
            if symbol == '.' or (symbol == '>' and (part_2 or direction == Direction.RIGHT)) or (symbol == '<' and (part_2 or direction == Direction.LEFT)) or (symbol == '^' and (part_2 or direction == Direction.UP)) or (symbol == 'v' and (part_2 or direction == Direction.DOWN)):
                hike.add(new_position)
                intersection = self.find_intersection(new_position, hike, part_2)
                if graph.has_edge(position, intersection):
                    continue # We have this calculated
                graph.add_node(intersection)
                graph.add_edge(position, intersection, weight=len(hike))
                self.branch(intersection, graph, part_2)

    def find_longest_path(self, graph: nx.DiGraph) -> int:
        longest_path = 0
        for edges in nx.all_simple_edge_paths(graph, self.start_position, self.end_position):
            path_length = 0
            for first, second in edges:
                # Node will be counted twice, so we need to subtract 1
                path_length += graph.get_edge_data(first, second)['weight'] - 1
            longest_path = max(longest_path, path_length)
        return longest_path


    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        graph = nx.DiGraph()
        graph.add_node(self.start_position)
        self.branch(self.start_position, graph, part_2)
        longest_path = self.find_longest_path(graph)
        print(f'Part {'2' if part_2 else '1'}: {longest_path} - {time.time() - start_time}')


def main() -> None:
    day = Day23()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
