from utilities.get_input import *
from utilities.parse import *
import time, re
from collections import defaultdict

class Day15:
    def __init__(self) -> None:
        self.input = get_input(2023, 15)
        self.parsed_input = parse_list(self.input)
        return

    def hash(self, input: str) -> int:
        sum = 0
        for char in input:
            sum += ord(char)
            sum *= 17
            sum %= 256
        return sum

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        sum = 0
        spliter = re.compile(r'\w+|\d+')
        if not part_2:
            for input in self.parsed_input:
                sum += self.hash(input)
        else:
            boxes = defaultdict(list)
            for input in self.parsed_input:
                instruction = re.findall(spliter, input)
                box_number =  self.hash(instruction[0])
                if len(instruction) > 1:
                    swapped = False
                    for i, lenses in enumerate(boxes[box_number]):
                        if lenses[0] == instruction[0]:
                            boxes[box_number].pop(i)
                            boxes[box_number].insert(i, (instruction[0], int(instruction[1])))
                            swapped = True
                    if not swapped:
                        boxes[box_number].append((instruction[0], int(instruction[1])))
                else:
                    for i, lenses in enumerate(boxes[box_number]):
                        if lenses[0] == instruction[0]:
                            boxes[box_number].pop(i)
                            break
            for box_key, lenses in boxes.items():
                for j, lens in enumerate(lenses):
                    sum += (box_key+1) * (j+1) * lens[1]
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day15()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
