from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from functools import cache

test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

class Day14:
    def __init__(self) -> None:
        self.input = test_input # get_input(2023, 14)
        self.grid = Grid(self.input)
        return
    
    @cache
    def roll_north(grid: Grid) -> Grid:
        size_x,size_y = grid.size()
        for y in range(size_y):
            for x in range(size_x):
                if grid.get(x, y) != 'O':
                    continue
                for y_above in range(y - 1, -1, -1):
                    if grid.get(x, y_above) == '.':
                        grid.set(x, y_above + 1, '.')
                        grid.set(x, y_above, 'O')
                    else:
                        break
        return grid

    @cache
    def roll_west(grid: Grid) -> Grid:
        size_x,size_y = grid.size()
        for x in range(size_x):
            for y in range(size_y):
                if grid.get(x, y) != 'O':
                    continue
                for x_left in range(x - 1, -1, -1):
                    if grid.get(x_left, y) == '.':
                        grid.set(x_left + 1, y, '.')
                        grid.set(x_left, y, 'O')
                    else:
                        break
        return grid

    @cache
    def roll_south(grid: Grid) -> Grid:
        size_x,size_y = grid.size()
        for y in range(size_y-1, -1, -1):
            for x in range(size_x):
                if grid.get(x, y) != 'O':
                    continue
                for y_below in range(y+1, size_y):
                    if grid.get(x, y_below) == '.':
                        grid.set(x, y_below - 1, '.')
                        grid.set(x, y_below, 'O')
                    else:
                        break
        return grid

    @cache
    def roll_east(grid: Grid) -> Grid:
        size_x,size_y = grid.size()
        for x in range(size_x-1, -1, -1):
            for y in range(size_y):
                if grid.get(x, y) != 'O':
                    continue
                for x_right in range(x + 1, size_x):
                    if grid.get(x_right, y) == '.':
                        grid.set(x_right - 1, y, '.')
                        grid.set(x_right, y, 'O')
                    else:
                        break
        return grid

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        size_x,size_y = self.grid.size()
        sum = 0
        if not part_2:
            self.grid = Day14.roll_north(self.grid)
        else:
            for _ in range(1000000000):
                self.grid = Day14.roll_north(self.grid)
                self.grid = Day14.roll_west(self.grid)
                self.grid = Day14.roll_south(self.grid)
                self.grid = Day14.roll_east(self.grid)
        for y in range(size_y):
            for x in range(size_x):
                if self.grid.get(x, y) == 'O':
                    sum += (size_y - y)
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day14()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
