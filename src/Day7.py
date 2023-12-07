from utilities.get_input import *
from utilities.parse import *
import time

test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

class Day7:
    def __init__(self) -> None:
        self.input = test_input # get_input(2023, 7)
        self.parsed_input = parse_lines(self.input)
        self.card_rank: dict[str, int] = {
            'A': 'A',
            'K': 'B',
            'Q': 'C', 
            'J': 'D',
            'T': 'E',
            '9': 'F',
            '8': 'G',
            '7': 'H',
            '6': 'I',
            '5': 'J',
            '4': 'K',
            '3': 'L',
            '2': 'M'}
        return

    def parse_hands(self, part_2: bool) -> list[str, int]:
        hands = []
        if part_2:
            self.card_rank['J'] = 'N'
        for line in self.parsed_input:
            hand, bid = line.split(' ')
            ranked_hand = [self.card_rank[card] for card in hand]
            hands.append((''.join(ranked_hand), int(bid)))
        return hands

    def value_hand(self, hand: tuple[str, int]) -> str:
        value = 0
        cards, bid = hand
        number_of_unique_cards = len(set(cards))
        number_of_most_common_card = max([cards.count(card) for card in cards])
        # Five of a kind is rank (5 - 1 = 4)
        # Four of a kind is rank (4 - 2 = 2)
        # Full house is rank (3 - 2 = 1)
        # Three of a kind is rank (3 - 3 = 0)
        # Two pair is rank (2 - 3 = -1)
        # One pair is rank (1 - 4 = -3)
        # High value is rank (5 - 1 = -4)
        rank = 4 - (number_of_most_common_card - number_of_unique_cards)
        return str(rank) + cards

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        hands = self.parse_hands(part_2)
        hands.sort(key=self.value_hand)
        winnings = 0
        for i, hand in enumerate(hands):
            cards, bid = hand
            winnings += bid * (i + 1)
        print(f'Part {'2' if part_2 else '1'}: {winnings} - {time.time() - start_time}')


def main() -> None:
    day = Day7()
    day.solve(False)
    day.solve(True)
    return


if __name__ == "__main__":
    main()
