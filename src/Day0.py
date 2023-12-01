from utilities.get_input import *
from utilities.parse import *
import time


class Day0:
    def __init__(self) -> None:
        self.input = get_input(2023, 0)
        self.parsed_input = parse_int(self.input)
        return

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        print(f'Part {'2' if part_2 else '1'}: {self.parsed_input} - {time.time() - start_time}')


def main() -> None:
    day = Day0()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
