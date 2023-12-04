from utilities.get_input import *
from utilities.parse import *
import time


class Day3:
    def __init__(self) -> None:
        self.input = get_input(2023, 3)
        self.parsed_input = parse_lines(self.input)
        self.numbers = self.parse_numbers()
        self.gears = self.parse_gears()
        return
    
    def parse_numbers(self) -> list[tuple[int, int, int, int]]:
        numbers: list[tuple[int, int, int, int]] = []
        for y, line in enumerate(self.parsed_input):
            number: str = ""
            for x, char in enumerate(line):
                if char.isdigit():
                    number += char
                    if x == line.__len__() - 1: 
                        numbers.append((parse_int(number), x - number.__len__() + 1, x, y))
                        number = ""
                elif number.__len__() > 0:
                    numbers.append((parse_int(number), x - number.__len__(), x - 1, y))
                    number = ""
        return numbers
    
    def parse_gears(self) -> list[tuple[int, int]]:
        gears: list[tuple[int, int]] = []
        for y, line in enumerate(self.parsed_input):
            for x, char in enumerate(line):
                if char == '*':
                   gears.append((x,y)) 
        return gears
    
    def get_symbol(self, x: int, y: int) -> str:
        if x < 0 or y < 0 or y >= self.parsed_input.__len__() or x >= self.parsed_input[y].__len__():
            return '.'
        return self.parsed_input[y][x]
    
    def check_symbol(self, number: tuple[int, int, int, int]) -> bool:
        # Check row above
        for x in range(number[1] - 1, number[2] + 2):
            symbol :str = self.get_symbol(x, number[3] - 1)
            if symbol != '.':
                return True
        # Check left
        symbol :str = self.get_symbol(number[1] - 1, number[3])
        if symbol != '.':
            return True
        # Check right
        symbol :str = self.get_symbol(number[2] + 1, number[3])
        if symbol != '.':
            return True
        # Check row below
        for x in range(number[1] - 1, number[2] + 2):
            symbol :str = self.get_symbol(x, number[3] + 1)
            if symbol != '.':
                return True
        return False
    
    def check_gears(self, number: tuple[int, int, int, int]) -> list[tuple[int, int]]:
        gears: list[tuple[int, int]] = []
        # Check row above
        for x in range(number[1] - 1, number[2] + 2):
            symbol :str = self.get_symbol(x, number[3] - 1)
            if symbol == '*':
                gears.append((x, number[3] - 1))
        # Check left
        symbol :str = self.get_symbol(number[1] - 1, number[3])
        if symbol == '*':
            gears.append((number[1] - 1, number[3]))
        # Check right
        symbol :str = self.get_symbol(number[2] + 1, number[3])
        if symbol == '*':
            gears.append((number[2] + 1, number[3]))
        # Check row below
        for x in range(number[1] - 1, number[2] + 2):
            symbol :str = self.get_symbol(x, number[3] + 1)
            if symbol == '*':
                gears.append((x, number[3] + 1))
        return gears

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        sum: int = 0
        gears_and_numbers: dict[tuple[int, int], list[int]] = {}
        for number in self.numbers:
            if part_2:
                gears:list[tuple[int, int]] = self.check_gears(number)
                for gear in gears:
                    if gear not in gears_and_numbers:
                        gears_and_numbers[gear] = [number[0]]
                    else:
                        gears_and_numbers[gear].append(number[0])
            elif self.check_symbol(number):
                sum += number[0]
        if part_2:
            for key in gears_and_numbers:
                mul = 1
                if gears_and_numbers[key].__len__() < 2:
                    continue
                for number in gears_and_numbers[key]:
                    mul *= number
                sum += mul
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day3()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
