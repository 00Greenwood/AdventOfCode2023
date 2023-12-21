from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from enum import Enum
from functools import cache

test_input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

type Position = tuple[int, int]

class Direction(Enum):
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1)
    DOWN = (0,1)

class Day21:
    def __init__(self) -> None:
        self.input = get_input(2023, 21)
        self.grid = Grid(self.input)
        return
    
    def reachable_plots(self, positions: set[Position], steps_remaining: int) -> set[Position]:
        new_steps_remaining = steps_remaining - 1
        new_positions = set()
        for position in positions:
            for direction in Direction:
                new_position = (position[0] + direction.value[0], position[1] + direction.value[1])
                new_symbol = self.grid.get(*new_position)
                if new_symbol == None:
                    continue
                if new_symbol != '#':      
                    new_positions.add(new_position)
        if new_steps_remaining == 0:
            return new_positions
        return self.reachable_plots(new_positions, new_steps_remaining)
            
    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        positions = set()
        positions.add(self.grid.find('S'))
        positions = self.reachable_plots(positions, 64)
        print(f'Part {'2' if part_2 else '1'}: {len(positions)} - {time.time() - start_time}')


def main() -> None:
    day = Day21()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
