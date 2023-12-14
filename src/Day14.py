from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid

class Day14:
    def __init__(self) -> None:
        self.input = get_input(2023, 14)
        self.grid = Grid()
        return
    
    def roll_north(self) -> None:
        size_x,size_y = self.grid.size()
        for y in range(size_y):
            for x in range(size_x):
                if self.grid.get(x, y) != 'O':
                    continue
                for y_above in range(y - 1, -1, -1):
                    if self.grid.get(x, y_above) == '.':
                        self.grid.set(x, y_above + 1, '.')
                        self.grid.set(x, y_above, 'O')
                    else:
                        break

    def roll_west(self) -> None:
        size_x,size_y = self.grid.size()
        for x in range(size_x):
            for y in range(size_y):
                if self.grid.get(x, y) != 'O':
                    continue
                for x_left in range(x - 1, -1, -1):
                    if self.grid.get(x_left, y) == '.':
                        self.grid.set(x_left + 1, y, '.')
                        self.grid.set(x_left, y, 'O')
                    else:
                        break

    def roll_south(self) -> None:
        size_x,size_y = self.grid.size()
        for y in range(size_y-1, -1, -1):
            for x in range(size_x):
                if self.grid.get(x, y) != 'O':
                    continue
                for y_below in range(y+1, size_y):
                    if self.grid.get(x, y_below) == '.':
                        self.grid.set(x, y_below - 1, '.')
                        self.grid.set(x, y_below, 'O')
                    else:
                        break

    def roll_east(self) -> None:
        size_x,size_y = self.grid.size()
        for x in range(size_x-1, -1, -1):
            for y in range(size_y):
                if self.grid.get(x, y) != 'O':
                    continue
                for x_right in range(x + 1, size_x):
                    if self.grid.get(x_right, y) == '.':
                        self.grid.set(x_right - 1, y, '.')
                        self.grid.set(x_right, y, 'O')
                    else:
                        break

    def calculate_load(self) -> int:
        size_x,size_y = self.grid.size()
        sum = 0
        for y in range(size_y):
            for x in range(size_x):
                if self.grid.get(x, y) == 'O':
                    sum += (size_y - y)
        return sum

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        self.grid = Grid(self.input)
        if not part_2:
            self.roll_north()
        else:
            current_load = self.calculate_load()
            previous_load = 0
            while previous_load != current_load:
                previous_load = current_load
                self.roll_north()
                self.roll_west()
                self.roll_south()
                self.roll_east()
                current_load = self.calculate_load()
        load = self.calculate_load()
        print(f'Part {'2' if part_2 else '1'}: {load} - {time.time() - start_time}')


def main() -> None:
    day = Day14()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
