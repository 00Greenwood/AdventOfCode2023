from get_input import *
from parse import *


class Day1:
    def __init__(self) -> None:
        self.input = get_input(2023, 1)
        self.parsed_input = parse_lines(self.input)
        return

    def solve_part_1(self) -> str:
        sum: int = 0
        for line in self.parsed_input:
            number: str = ""
            # Find the first number in the line
            for char in line:
                if char.isdigit():
                    number += char
                    break
            # Find the last number in the line
            for char in line[::-1]:
                if char.isdigit():
                    number += char
                    break
            sum += parse_int(number)
        return str(sum)

    def solve_part_2(self) -> str:
        sum: int = 0
        allowedDigits: dict[str, str] = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
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
            firstIndex: int = line.__len__()
            firstDigit: str = ""
            lastIndex: int = -1
            lastDigit: str = ""
            # Iterate over the allowed digits and find the first and last one in the line
            for allowedDigit in allowedDigits:
                index = line.find(allowedDigit)
                if (index >= 0) and (index < firstIndex):
                    firstIndex = index
                    firstDigit = allowedDigits[allowedDigit]
                index = line.rfind(allowedDigit)
                if (index >= 0) and (index > lastIndex):
                    lastIndex = index
                    lastDigit = allowedDigits[allowedDigit]
            sum += parse_int(firstDigit + lastDigit)
        return str(sum)


def main() -> None:
    day = Day1()
    print(day.solve_part_1())
    print(day.solve_part_2())
    return


if __name__ == "__main__":
    main()
