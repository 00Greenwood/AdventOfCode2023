from utilities.get_input import *
from utilities.parse import *
import time, sys
from utilities.Grid import Grid
from enum import Enum

sys.setrecursionlimit(100000)

test_input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

type Position = tuple[int, int]
type Hike = set[Position]

class Direction(Enum):
    RIGHT = (1,  0)
    LEFT =  (-1, 0)
    UP =    (0, -1)
    DOWN =  (0,  1)

class Day23:
    def __init__(self) -> None:
        self.input = test_input # get_input(2023, 23)
        self.maze = Grid(self.input)
        self.max_hike_length = 0
        return
    
    def append_to_hike_and_find_hikes(self, position: Position, end_position: Position, hike: Hike, part_2: bool) -> None:
        hike.add(position)
        self.find_hikes(position, end_position, hike, part_2)
        hike.remove(position)

    def find_hikes(self, position: Position, end_position: Position, hike: Hike, part_2: bool):
        for direction in Direction:
            new_position = (position[0] + direction.value[0], position[1] + direction.value[1])
            if new_position in hike:
                continue # We have already been here
            if new_position == end_position:
                self.max_hike_length = max(self.max_hike_length, len(hike))
                print(f'Current max: {self.max_hike_length}')
                return # We have reached the end
            symbol = self.maze.get(*new_position)
            if symbol == None or symbol == '#':
                continue # We can not go here
            if symbol == '.':
                self.append_to_hike_and_find_hikes(new_position, end_position, hike, part_2)
            elif symbol == '>' and (part_2 or direction == Direction.RIGHT):
                self.append_to_hike_and_find_hikes(new_position, end_position, hike, part_2)
            elif symbol == '<' and (part_2 or direction == Direction.LEFT):
                self.append_to_hike_and_find_hikes(new_position, end_position, hike, part_2)
            elif symbol == '^' and (part_2 or direction == Direction.UP):
                self.append_to_hike_and_find_hikes(new_position, end_position, hike, part_2)
            elif symbol == 'v' and (part_2 or direction == Direction.DOWN):
                self.append_to_hike_and_find_hikes(new_position, end_position, hike, part_2)

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        start_position = (1, 0)
        end_position = (self.maze.max_x - 1, self.maze.max_y)
        hike: set(Position) = {start_position}
        self.find_hikes(start_position, end_position, hike, part_2)
        print(f'Part {'2' if part_2 else '1'}: {self.max_hike_length} - {time.time() - start_time}')


def main() -> None:
    day = Day23()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
