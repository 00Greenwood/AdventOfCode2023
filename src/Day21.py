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
                if new_symbol != '#':      
                    new_positions.add(new_position)
        if new_steps_remaining == 0:
            return new_positions
        return self.reachable_plots(new_positions, new_steps_remaining)
            
    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        output = 0
        if not part_2:    
            positions = set()
            positions.add(self.grid.find('S'))
            positions = self.reachable_plots(positions, 64)
            output = len(positions)
        if part_2:
            # As the input is a repeating square with no "#" in the horizontal or vertical lines, the reachable plots will expand at a predictable rate.
            # This is calculates by counting the number of reachable plots for f(65), f(65 + 131), f(65 + 2*131)
            # Which are 3859, 34324 and 95135, calculated from the code in part 1.
            # Therefore, the number of reachable plots is 3859 + 15292x + 15173x^2 where x is the number of grids.
            # Wolfram Alpha to the rescue!
            number_of_grids = (26501365 - 65) / 131
            output = int(3859 + 15292 * number_of_grids + 15173 * number_of_grids**2)
        print(f'Part {'2' if part_2 else '1'}: {output} - {time.time() - start_time}')


def main() -> None:
    day = Day21()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
