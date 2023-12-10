from utilities.get_input import *
from utilities.parse import *
from utilities.Grid import Grid
import time

class Day10:
    def __init__(self) -> None:
        self.input = get_input(2023, 10)
        self.grid = Grid(self.input)
        return
    
    def start_of_loop(self, start: tuple[int, int]) -> tuple[int, int]:
        north = self.grid.get(start[0], start[1] - 1)
        south = self.grid.get(start[0], start[1] + 1)
        east = self.grid.get(start[0] + 1, start[1])
        west = self.grid.get(start[0] - 1, start[1])
        if north == "|" or north == "7" or north == "F":
            return (start[0], start[1] - 1)
        if south == "|" or south == "L" or south == "J":
            return (start[0], start[1] + 1)
        if east == "-" or east == "J" or east == "7":
            return (start[0] + 1, start[1])
        if west == "-" or west == "L" or west == "F":
            return (start[0] - 1, start[1])
        
    def find_next_position(self, previous_position: tuple[int, int], current_position: tuple[int, int]) -> tuple[int, int]:
        x,y = current_position
        next_pipe = self.grid.get(x, y)
        if next_pipe == "-":
            if previous_position[0] == x + 1:
                return (x - 1, y)
            else:
                return (x + 1, y)
        if next_pipe == "|":
            if previous_position[1] == y + 1:
                return (x, y - 1)
            else:
                return (x, y + 1)
        if next_pipe == "L":
            if previous_position[0] == x + 1:
                return (x, y - 1)
            else:
                return (x + 1, y)
        if next_pipe == "J":
            if previous_position[1] == y - 1:
                return (x - 1, y)
            else:
                return (x, y - 1)
        if next_pipe == "7":
            if previous_position[0] == x - 1:
                return (x, y + 1)
            else:
                return (x - 1, y)
        if next_pipe == "F":
            if previous_position[1] == y + 1:
                return (x + 1, y)
            else:
                return (x, y + 1)


    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        start = self.grid.find("S")
        # Find where the loop begins from the start
        loop: list(tuple[int, int]) = []
        start_of_loop = self.start_of_loop(start)
        loop.append(start_of_loop)
        # Find the loop
        previous_position = start
        current_position = loop[-1]
        while current_position != start:
            next_position = self.find_next_position(previous_position, current_position)
            previous_position = current_position
            current_position = next_position
            loop.append(current_position)
        distance = int(len(loop) / 2)
        if part_2:
            count = 0
            max_x, max_y = self.grid.size()
            for y in range(0, max_y):
                number_of_intersections = 0
                for x in range(0, max_x):
                    pipe = self.grid.get(x, y)
                    if (x, y) in loop and (pipe == "|" or pipe == "J" or pipe == "L"):  
                        number_of_intersections += 1
                    if (x,y) not in loop and number_of_intersections % 2 != 0:
                        count += 1
            distance = count
        print(f'Part {'2' if part_2 else '1'}: {distance} - {time.time() - start_time}')


def main() -> None:
    day = Day10()
    day.solve(False)
    day.solve(True) 
    return


if __name__ == "__main__":
    main()
