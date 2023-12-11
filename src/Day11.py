from utilities.get_input import *
from utilities.parse import *
from utilities.Grid import Grid
import time

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

class Day11:
    def __init__(self) -> None:
        self.input = get_input(2023, 11)
        self.parsed_input = Grid(self.input)
        self.galaxies = self.parsed_input.find_all('#')
        return
    
    def expand_galaxies(self, expansion: int) -> list[tuple[int,int]]:
        new_galaxies: list[tuple[int,int]] = []
        x_values = [galaxy[0] for galaxy in self.galaxies]
        empty_rows = []
        for x in range(max(x_values)):
            if x not in x_values:
                empty_rows.append(x)
        y_values = [galaxy[1] for galaxy in self.galaxies]
        empty_columns = []
        for y in range(max(y_values)):
            if y not in y_values:
                empty_columns.append(y)
        for galaxy in self.galaxies:
            x, y = galaxy
            new_x = x + (expansion * sum([int(row < x) for row in empty_rows]))
            new_y = y + (expansion * sum([int(column < y) for column in empty_columns]))
            new_galaxies.append((new_x, new_y))
        return new_galaxies

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        galaxies = self.expand_galaxies(999999 if part_2 else 1)
        sum = 0
        for i, galaxy in enumerate(galaxies):
            for j in range(i + 1, len(galaxies)):
                second_galaxy = galaxies[j]
                # Manhattan distance
                distance = abs(galaxy[0] - second_galaxy[0]) + abs(galaxy[1] - second_galaxy[1])
                sum += distance
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day11()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
