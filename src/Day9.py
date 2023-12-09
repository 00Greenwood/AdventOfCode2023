from utilities.get_input import *
from utilities.parse import *
import time

class Day9:
    def __init__(self) -> None:
        self.input = get_input(2023, 9)
        self.parsed_input = parse_lines(self.input)
        self.sequences = self.parse_sequences()
        return
    
    def parse_sequences(self) -> list[list[int]]:
        sequences = []
        for line in self.parsed_input:
            sequences.append([int(number) for number in line.split(' ')])
        return sequences
    
    def get_next_number(self, sequence: list[int]) -> int:
        differences: list[int] = []
        for i in range(0, len(sequence) - 1):
            differences.append(sequence[i+1] - sequence[i])    
        if max(differences) == 0 and min(differences) == 0:
            return sequence[-1]
        return sequence[-1] + self.get_next_number(differences)
    
    def get_previous_number(self, sequence: list[int]) -> int:
        differences: list[int] = []
        for i in range(0, len(sequence) - 1):
            differences.append(sequence[i+1] - sequence[i])    
        if max(differences) == 0 and min(differences) == 0:
            return sequence[0]
        return sequence[0] - self.get_previous_number(differences)

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        next_numbers:list[int] = []
        for sequence in self.sequences:
            if part_2:
                next_numbers.append(self.get_previous_number(sequence))
            else:
                next_numbers.append(self.get_next_number(sequence))
        print(f'Part {'2' if part_2 else '1'}: {sum(next_numbers)} - {time.time() - start_time}')


def main() -> None:
    day = Day9()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
