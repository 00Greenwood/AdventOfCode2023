from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from queue import SimpleQueue
from enum import Enum

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
        self.input = get_input(2023, 23)
        self.maze = Grid(self.input)
        return
    
    def append_to_hike(self, positions_to_check: SimpleQueue, hike: Hike, positions: set[Position]) -> Hike:
        for position in positions:
            # Only copy the hike if we need to
            new_hike = hike.copy() if len(positions) > 1 else hike
            new_hike.add(position)
            positions_to_check.put((position, new_hike))

    def find_hikes(self, part_2: bool) -> list[Hike]:
        start_position = (1, 0)
        end_position = (self.maze.max_x - 1, self.maze.max_y)
        hike_lengths = list()
        positions_to_check: SimpleQueue[tuple[Position, Hike]] = SimpleQueue()
        positions_to_check.put((start_position, {start_position}))
        while not positions_to_check.empty():
            position, hike = positions_to_check.get()
            new_positions_to_check = set()
            for direction in Direction:
                new_position = (position[0] + direction.value[0], position[1] + direction.value[1])
                if new_position in hike:
                    continue # We have already been here
                if new_position == end_position:
                    hike_lengths.append(hike)
                    continue # We have reached the end
                symbol = self.maze.get(*new_position)
                if symbol == None or symbol == '#':
                    continue # We can not go here
                if symbol == '.':
                    new_positions_to_check.add(new_position)
                elif symbol == '>' and (part_2 or direction == Direction.RIGHT):
                    new_positions_to_check.add(new_position)
                elif symbol == '<' and (part_2 or direction == Direction.LEFT):
                    new_positions_to_check.add(new_position)
                elif symbol == '^' and (part_2 or direction == Direction.UP):
                    new_positions_to_check.add(new_position)
                elif symbol == 'v' and (part_2 or direction == Direction.DOWN):
                    new_positions_to_check.add(new_position)
            self.append_to_hike(positions_to_check, hike, new_positions_to_check)
        return hike_lengths

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        hikes = self.find_hikes(part_2)
        max_hike = max(hikes, key=lambda hike: len(hike))
        print(f'Part {'2' if part_2 else '1'}: {len(max_hike)} - {time.time() - start_time}')


def main() -> None:
    day = Day23()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
