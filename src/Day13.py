from utilities.get_input import *
from utilities.parse import *
import time, re
from utilities.Grid import Grid

class Day13:
    def __init__(self) -> None:
        self.input = get_input(2023, 13)
        self.parsed_input = re.split(r'\n\n', self.input.strip())
        self.grids = [Grid(block) for block in self.parsed_input]
        return
    
    def check_column(grid: Grid, x: int, negative_x: int) -> bool:
        return grid.get_column(x) == grid.get_column(negative_x)
    
    def check_row(grid: Grid, y: int, negative_y: int) -> bool:
        return grid.get_row(y) == grid.get_row(negative_y)
        
    def check_x_split(grid: Grid, split_x: int, size_x: int) -> bool:
        columns_to_check = min(split_x, size_x - split_x)
        for x in range(split_x, split_x + columns_to_check):
            negative_x = split_x - (x - split_x) - 1
            if not Day13.check_column(grid, x, negative_x):
                return False
        return True
    
    def check_y_split(grid: Grid, split_y: int, size_y: int) -> bool:
        row_to_check = min(split_y, size_y - split_y)
        for y in range(split_y, split_y + row_to_check):
            negative_y = split_y - (y - split_y) - 1
            if not Day13.check_row(grid, y, negative_y):
                return False
        return True
    
    def check_reflection(grid: Grid, ignore_reflection: tuple[int, int] = (-1,-1)) -> tuple[int, int]:
        size_x, size_y = grid.size()
        # Check columns
        for split_x in range(1, size_x):
            if Day13.check_x_split(grid, split_x, size_x) and (split_x, 0) != ignore_reflection:
                return (split_x, 0)
        # Check rows
        for split_y in range(1, size_y):
            if Day13.check_y_split(grid, split_y, size_y) and (0, split_y) != ignore_reflection:
                return (0, split_y)
        raise Exception('No reflection found!')

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        vertical_reflections = 0
        horizontal_reflections = 0
        for grid in self.grids:
            original_reflections = Day13.check_reflection(grid)
            if not part_2:
                vertical_reflections += original_reflections[0]
                horizontal_reflections += original_reflections[1]
            else:
                for x,y in grid.keys():
                    original = grid.get(x, y)
                    if original == ".":
                        grid.set(x, y, "#")
                    else :
                        grid.set(x, y, ".")
                    try:
                        reflections = Day13.check_reflection(grid, original_reflections)
                        vertical_reflections += reflections[0]
                        horizontal_reflections += reflections[1]
                        break
                    except:
                        # Do nothing
                        pass
                    grid.set(x, y, original)

        print(f'Part {'2' if part_2 else '1'}: {horizontal_reflections * 100 + vertical_reflections} - {time.time() - start_time}')


def main() -> None:
    day = Day13()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
