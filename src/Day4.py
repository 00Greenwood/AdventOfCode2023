from utilities.get_input import *
from utilities.parse import *
import time, re


class Day4:
    def __init__(self) -> None:
        self.input = get_input(2023, 4)
        self.parsed_input = parse_lines(self.input)
        self.cards = self.parse_cards()
        return
    
    def parse_cards(self) -> list[tuple[list[str], list[str]]]:
        cards: list[tuple[list[str], list[str]]] = []
        for line in self.parsed_input:
            card_number, numbers = re.split(r':\s+', line)
            winning_numbers, selected_numbers =  re.split(r'\s+\|\s+', numbers)
            cards.append((re.split(r'\s+', winning_numbers), re.split(r'\s+', selected_numbers)))
        return cards


    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        sum = 0
        copies: list[int] = [1 for _ in range(self.cards.__len__())]
        for i, card in enumerate(self.cards):
            winning_numbers, selected_numbers = card
            if part_2:
                number_of_winning = 0
                for winning_number in winning_numbers:
                    if winning_number in selected_numbers:
                        number_of_winning += 1
                for j in range(i + 1, i + number_of_winning + 1):
                    copies[j] += copies[i]
                sum += copies[i]
            else:
                exponent = 0
                for winning_number in winning_numbers:
                    if winning_number in selected_numbers:
                        exponent += 1
                if exponent > 0:
                    sum += 2 ** (exponent - 1)
        print(f'Part {'2' if part_2 else '1'}: {sum} - {time.time() - start_time}')


def main() -> None:
    day = Day4()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
