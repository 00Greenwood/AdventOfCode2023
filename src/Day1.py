from utilities.get_input import *
from utilities.parse import *
import time

class Day1:
    def __init__(self) -> None:
        self.input = get_input(2023, 1)
        self.parsed_input = parse_lines(self.input)
        return

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        sum: int = 0
        digits: dict[str, str] = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        for line in self.parsed_input:
            first_index: int = line.__len__()
            first_digit: str = ""
            last_index: int = -1
            last_digit: str = ""
            # Iterate over the digits values and find the first and last one in the line
            for digit in digits.values():
                index = line.find(digit)
                if (index >= 0) and (index < first_index):
                    first_index = index
                    first_digit = digit
                index = line.rfind(digit)
                if (index >= 0) and (index > last_index):
                    last_index = index
                    last_digit = digit
            if part_2:
                # For part 2, also iterate over the keys
                for digit in digits.keys():
                    index = line.find(digit)
                    if (index >= 0) and (index < first_index):
                        first_index = index
                        first_digit = digits[digit]
                    index = line.rfind(digit)
                    if (index >= 0) and (index > last_index):
                        last_index = index
                        last_digit = digits[digit]
            sum += parse_int(first_digit + last_digit)
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}ms')


def main() -> None:
    day = Day1()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
