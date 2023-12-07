from utilities.get_input import *
from utilities.parse import *
import time

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


class Day7:
    def __init__(self) -> None:
        self.input = get_input(2023, 7)
        self.parsed_input = parse_lines(self.input)
        self.card_rank: dict[str, int] = {'A': 14, 'K': 13, 'Q': 12, 'J': 11,
                                          'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
        return

    def parse_hands(self, part_2: bool) -> list[tuple[tuple[int, int, int, int, int], int]]:
        hands = []
        if part_2:
            self.card_rank['J'] = 1
        for line in self.parsed_input:
            hand, bid = line.split(' ')
            first, second, third, fourth, fifth = [
                self.card_rank[card] for card in hand]
            hands.append(((first, second, third, fourth, fifth), int(bid)))
        return hands

    def value_hand(self, hand: tuple[tuple[int, int, int, int, int], int]) -> int:
        value = 0
        cards, bid = hand
        for i, card in enumerate(cards):
            value += card * (100 ** (4 - i))
        number_of_unique_cards = len(set(cards))
        number_of_most_common_card = max([cards.count(card) for card in cards])
        # Jokers are worth 1 in part 2 and can be anything
        number_of_jokers = cards.count(1)
        # Five of a kind
        if (number_of_unique_cards == 1):
            value *= (100 ** 6)
        # Four of a kind with a joker is actually five of a kind
        elif (number_of_unique_cards == 2 and number_of_most_common_card == 4 and number_of_jokers > 0):
            value *= (100 ** 6)
        # Four of a kind
        elif (number_of_unique_cards == 2 and number_of_most_common_card == 4):
            value *= (100 ** 5)
        # Full house with jokers is actually five of a kind
        elif (number_of_unique_cards == 2 and number_of_most_common_card == 3 and number_of_jokers > 0):
            value *= (100 ** 6)
        # Full house
        elif (number_of_unique_cards == 2 and number_of_most_common_card == 3):
            value *= (100 ** 4)
        # Three of a kind with a joker is actually four of a kind
        elif (number_of_unique_cards == 3 and number_of_most_common_card == 3 and number_of_jokers > 0):
            value *= (100 ** 5)
        # Three of a kind
        elif (number_of_unique_cards == 3 and number_of_most_common_card == 3):
            value *= (100 ** 3)
        # Two pair with jokers is actually four of a kind
        elif (number_of_unique_cards == 3 and number_of_most_common_card == 2 and number_of_jokers > 1):
            value *= (100 ** 5)
        # Two pair with a joker is actually a full house
        elif (number_of_unique_cards == 3 and number_of_most_common_card == 2 and number_of_jokers > 0):
            value *= (100 ** 4)
        # Two pair
        elif (number_of_unique_cards == 3 and number_of_most_common_card == 2):
            value *= (100 ** 2)
        # One pair with a joker is actually three of a kind
        elif (number_of_unique_cards == 4 and number_of_jokers > 0):
            value *= (100 ** 3)
        # One pair
        elif (number_of_unique_cards == 4):
            value *= 100
        # High value with a joker is actually one pair
        elif (number_of_unique_cards == 5 and number_of_jokers > 0):
            value *= 100
        return value

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
