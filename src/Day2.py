from utilities.get_input import *
from utilities.parse import *
import time


class Day2:
    def __init__(self) -> None:
        self.input = get_input(2023, 2)
        self.parsed_input = parse_lines(self.input)
        return

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        sum = 0
        for game in self.parsed_input:
            max_reds = 0
            max_blues = 0
            max_greens = 0
            game_id, game_rounds = game.split(': ')
            game_number = parse_int(game_id.split(' ')[1])
            rounds = game_rounds.split('; ')
            for round in rounds:
                cubes = round.split(', ')
                for cube in cubes:
                    number, color = cube.split(' ')
                    if color == 'red':
                        max_reds = max(max_reds, parse_int(number))
                    elif color == 'blue':
                        max_blues = max(max_blues, parse_int(number))
                    elif color == 'green':
                        max_greens = max(max_greens, parse_int(number))
            if part_2:
                sum += max_reds * max_blues * max_greens           
            elif max_reds <= 12 and max_greens <= 13 and max_blues <= 14:
                sum += game_number
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day2()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
