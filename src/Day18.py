from utilities.get_input import *
from utilities.parse import *
import time, re
from enum import Enum

class Direction(Enum):
    R = (1,0)
    L = (-1,0)
    U = (0,-1)
    D = (0,1)

type Position = tuple[int, int]

class Day18:
    def __init__(self) -> None:
        self.input = get_input(2023, 18)
        self.parsed_input = parse_lines(self.input)
        return
    
    def construct_trench(self, part_2: bool) -> list[Position]:
        matcher = re.compile(r'\w+|\d+')
        trench: list[Position] = list()
        position = (0,0)
        trench.append(position)
        for line in self.parsed_input:
            direction_str, length_str, colour = matcher.findall(line)
            length = int(length_str)
            direction = Direction[direction_str].value
            if part_2:
                if colour[5] == '0':
                    direction = Direction.R.value
                elif colour[5] == '1':
                    direction = Direction.D.value
                elif colour[5] == '2':
                    direction = Direction.L.value
                elif colour[5] == '3':
                    direction = Direction.U.value
                length = int(colour[0:5], 16)
            position = (position[0] + length * direction[0], position[1] + length * direction[1])
            trench.append(position)
        return trench
    
    def calculate_interior(self, trench: list[Position]) -> int:
        area = 0
        # https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
        for i in range(len(trench) - 1):
            area += 0.5 * (trench[i+1][0] + trench[i][0]) * (trench[i+1][1] - trench[i][1])
        boundary_points = 0
        for i in range(len(trench) - 1):
            boundary_points += abs(trench[i+1][0] - trench[i][0]) + abs(trench[i+1][1] - trench[i][1])
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        interior_points = area - (boundary_points * 0.5) + 1
        return int(interior_points + boundary_points)
    
    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        trench = self.construct_trench(part_2)
        lava_volume = self.calculate_interior(trench)
        print(f'Part {'2' if part_2 else '1'}: {lava_volume} - {time.time() - start_time}')


def main() -> None:
    day = Day18()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
