from utilities.get_input import *
from utilities.parse import *


class Day2:
    def __init__(self) -> None:
        self.input = get_input(2023, 2)
        self.parsed_input = parse_int(self.input)
        return

    def solve_part_1(self) -> str:
        return str(self.parsed_input)

    def solve_part_2(self) -> str:
        return str(self.parsed_input)


def main() -> None:
    day = Day2()
    print(day.solve_part_1())
    print(day.solve_part_2())
    return


if __name__ == "__main__":
    main()
