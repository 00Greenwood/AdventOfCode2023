from utilities.get_input import *
from utilities.parse import *
import time, re, math

class Day6:
    def __init__(self) -> None:
        self.input = get_input(2023, 6)
        self.parsed_input = parse_lines(self.input)
        self.races = self.parse_races()
        return
    
    def parse_races(self)-> list(tuple[int, int]):
        races:list(tuple[int, int]) = []
        times = re.findall(r'\d+', self.parsed_input[0])
        distance = re.findall(r'\d+', self.parsed_input[1])
        for i in range(len(times)):
            races.append((int(times[i]), int(distance[i])))
        return races
    
    def solve_equation(self, a: int, b: int, c: int) -> tuple[float, float]:
        discriminant = (b ** 2 - 4 * a * c) ** (1 / 2)
        x_1 = (-b + discriminant) / (2 * a)
        x_2 = (-b - discriminant) / (2 * a)
        return (x_1, x_2)

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        mul: int = 1
        if not part_2:    
            for race_time, distance in self.races:
                sum: int = 0
                for speed in range(1, race_time):
                    distance_traveled = speed * (race_time - speed)
                    if distance_traveled > distance:
                        sum += 1
                mul *= sum
        else:
            race_time: int = 0
            distance: int = 0
            for races in self.races:
                race_time = int(str(race_time) + str(races[0]))
                distance = int(str(distance) + str(races[1]))
            x_1, x_2 = self.solve_equation(-1, race_time, -distance)
            mul = math.floor(x_2) - math.ceil(x_1) + 1
        print(f'Part {'2' if part_2 else '1'}: {mul} - {time.time() - start_time}')


def main() -> None:
    day = Day6()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
