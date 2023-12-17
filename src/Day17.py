from utilities.get_input import *
from utilities.parse import *
import time
from utilities.Grid import Grid
from queue import PriorityQueue
from enum import Enum
from dataclasses import dataclass, field

class Direction(Enum):
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1)
    DOWN = (0,1)

    def is_opposite(self, other) -> bool:
        return self.value[0] == -other.value[0] and self.value[1] == -other.value[1]

type Position = tuple[int, int]
type PositionToCheck = tuple[Position, int,]

@dataclass(order=True)
class PrioritizedItem:
    heat_loss: int
    position: Position=field(compare=False)
    previous_direction: Direction=field(compare=False)
    steps: int=field(compare=False)

    def decompose(self) -> tuple[int, Position, Direction, int]:
        return (self.heat_loss, self.position, self.previous_direction, self.steps)

class Day17:
    def __init__(self) -> None:
        self.input = get_input(2023, 17)
        self.grid = Grid(self.input, True)
        self.max_x, self.max_y = self.grid.max()
        self.end_position = (self.max_x, self.max_y)
        return
    
    def dijkstra(self, part_2: bool) -> int:
        max_steps = 10 if part_2 else 3
        min_steps = 4 if part_2 else 0
        positions_to_check: PriorityQueue[PrioritizedItem] = PriorityQueue()
        positions_to_check.put(PrioritizedItem(self.grid.get(1,0), (1,0), Direction.RIGHT, 1))
        positions_to_check.put(PrioritizedItem(self.grid.get(0,1), (0,1), Direction.DOWN, 1))
        visited_positions: set[tuple[position, Direction, int]] = set()
        while positions_to_check.qsize() > 0:
            heat_loss, position, previous_direction, steps = positions_to_check.get().decompose()
            # Cache visited positions
            if (position, previous_direction, steps) in visited_positions:
                continue # We have already been here
            visited_positions.add((position, previous_direction, steps))

            for direction in Direction:
                if direction.is_opposite(previous_direction):
                    continue # We can not go backward
                if direction == previous_direction:
                    new_steps = steps + 1
                else:
                    new_steps = 1
                    if steps < min_steps:
                        continue # We can not turn before we have gone a minimum number of steps
                if new_steps > max_steps:
                    continue # We can not go straight for more than a maximum number of steps
                next_position = (position[0] + direction.value[0], position[1] + direction.value[1])
                if next_position[0] < 0 or next_position[0] > self.max_x or next_position[1] < 0 or next_position[1] > self.max_y:
                    continue # Outside of grid
                next_heat_loss = heat_loss + self.grid.get(*next_position)
                if next_position == self.end_position:
                    return next_heat_loss
                positions_to_check.put(PrioritizedItem(next_heat_loss, next_position, direction, new_steps))

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        heat_loss = self.dijkstra(part_2)
        print(f'Part {'2' if part_2 else '1'}: {heat_loss} - {time.time() - start_time}')


def main() -> None:
    day = Day17()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
