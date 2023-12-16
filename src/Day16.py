from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from enum import Enum
from queue import Queue

test_input = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


class Direction(Enum):
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1)
    DOWN = (0,1)

type Position = tuple[int, int]
type PositionWithDirection = tuple[Position, Direction]

class Day16:
    def __init__(self) -> None:
        self.input = get_input(2023, 16)
        self.grid = Grid(self.input)
        self.max_x, self.max_y = self.grid.max()
        return
    
    def move_and_check_path(self, position: Position, direction: Direction, positions_to_check: Queue[PositionWithDirection], path: list[PositionWithDirection]) -> None:
        position = (position[0] + direction.value[0], position[1] + direction.value[1])
        position_with_direction = (position, direction)
        if position[0] < 0 or position[0] > self.max_x or position[1] < 0 or position[1] > self.max_y:
            return
        if position_with_direction not in path:
            positions_to_check.put(position_with_direction)
            path.append(position_with_direction)

    def move_through_vertical_splitter(self, position: Position, direction: Direction, positions_to_check: Queue[PositionWithDirection], path: list[PositionWithDirection]) -> None:
        if direction == Direction.UP or direction == Direction.DOWN: # Treat as empty
            self.move_and_check_path(position, direction, positions_to_check, path)
        else:  # Split!
            self.move_and_check_path(position, Direction.UP, positions_to_check, path)
            self.move_and_check_path(position, Direction.DOWN, positions_to_check, path)

    def move_through_horizontal_splitter(self, position: Position, direction: Direction, positions_to_check: Queue[PositionWithDirection], path: list[PositionWithDirection]) -> None:
        if direction == Direction.LEFT or direction == Direction.RIGHT: # Treat as empty
            self.move_and_check_path(position, direction, positions_to_check, path)
        else:  # Split!
            self.move_and_check_path(position, Direction.LEFT, positions_to_check, path)
            self.move_and_check_path(position, Direction.RIGHT, positions_to_check, path)

    def move_through_back_mirror(self, position: Position, direction: Direction, positions_to_check: Queue[PositionWithDirection], path: list[PositionWithDirection]) -> None:
        if direction == Direction.LEFT:
            self.move_and_check_path(position, Direction.UP, positions_to_check, path)
        elif direction == Direction.RIGHT:
            self.move_and_check_path(position, Direction.DOWN, positions_to_check, path)
        elif direction == Direction.UP:
            self.move_and_check_path(position, Direction.LEFT, positions_to_check, path)
        elif direction == Direction.DOWN:
            self.move_and_check_path(position, Direction.RIGHT, positions_to_check, path)  

    def move_through_forward_mirror(self, position: Position, direction: Direction, positions_to_check: Queue[PositionWithDirection], path: list[PositionWithDirection]) -> None:
        if direction == Direction.LEFT:
            self.move_and_check_path(position, Direction.DOWN, positions_to_check, path)
        elif direction == Direction.RIGHT:
            self.move_and_check_path(position, Direction.UP, positions_to_check, path)
        elif direction == Direction.UP:
            self.move_and_check_path(position, Direction.RIGHT, positions_to_check, path)
        elif direction == Direction.DOWN:
            self.move_and_check_path(position, Direction.LEFT, positions_to_check, path) 
            
    def calculate_energized(self, start_position: Position, start_direction: Direction) -> int:
        path: list[PositionWithDirection] = list()
        energized: set[Position] = set()
        positions_to_check: Queue[PositionWithDirection] = Queue()
        self.move_and_check_path(start_position, start_direction, positions_to_check, path)
        while positions_to_check.qsize() > 0:
            position, direction = positions_to_check.get()
            symbol = self.grid.get(position[0], position[1]) 
            if symbol == ".":
                self.move_and_check_path(position, direction, positions_to_check, path)
            elif symbol == "|":
                self.move_through_vertical_splitter(position, direction, positions_to_check, path)
            elif symbol == "-":
                self.move_through_horizontal_splitter(position, direction, positions_to_check, path)
            elif symbol == "\\":
                self.move_through_back_mirror(position, direction, positions_to_check, path)
            elif symbol == "/":              
                self.move_through_forward_mirror(position, direction, positions_to_check, path)
            else:
                raise Exception("Unknown symbol!")
        for entry in path:
            energized.add(entry[0])
        return len(energized) 


    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        energized_number = 0
        if not part_2:
            energized_number = self.calculate_energized((-1,0), Direction.RIGHT)
        else:
            energized_numbers: list[int] = []
            for y in range(self.max_y + 1): 
                energized_numbers.append(self.calculate_energized((-1, y), Direction.RIGHT))
                energized_numbers.append(self.calculate_energized((self.max_x + 1, y), Direction.LEFT))
            for x in range(self.max_x + 1):
                energized_numbers.append(self.calculate_energized((x, -1), Direction.DOWN))
                energized_numbers.append(self.calculate_energized((x, self.max_y + 1), Direction.UP))
            energized_number = max(energized_numbers)
        print(f'Part {'2' if part_2 else '1'}: {energized_number} - {time.time() - start_time}')


def main() -> None:
    day = Day16()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
