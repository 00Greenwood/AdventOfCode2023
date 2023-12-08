from utilities.get_input import *
from utilities.parse import *
import time

class Day7:
    def __init__(self) -> None:
        self.input = get_input(2023, 7)
        self.parsed_input = parse_lines(self.input)
        self.card_rank: dict[str, int] = {'A': 'A', 'K': 'B', 'Q': 'C', 'J': 'D',
                                          'T': 'E', '9': 'F', '8': 'G', '7': 'H', '6': 'I', '5': 'J', '4': 'K', '3': 'L', '2': 'M'}
        return

    def parse_hands(self, part_2: bool) -> list[str, int]:
        hands = []
        if part_2:
            self.card_rank['J'] = 'N'
        for line in self.parsed_input:
            hand, bid = line.split(' ')
            new_hand = "".join([self.card_rank[card] for card in hand])
            hands.append((new_hand, int(bid)))
        return hands

    def value_hand(self, hand: tuple[str, int]) -> str:
        cards, bid = hand
        number_of_unique_cards = len(set(cards))
        number_of_most_common_card = max([cards.count(card) for card in cards])
        rank_of_hand = number_of_most_common_card - number_of_unique_cards
        # Jokers are worth 1 in part 2 and can be anything
        number_of_jokers = cards.count('N')
        # Five of a kind
        if (rank_of_hand == 4):
            cards = '1' + cards
        # Four of a kind
        elif (rank_of_hand == 2):
            if (number_of_jokers > 0):
                cards = '1' + cards
            else:
                cards = '2' + cards
        # Full house
        elif (rank_of_hand == 1):
            if (number_of_jokers > 0):
                cards = '1' + cards
            else:
                cards = '3' + cards
        # Three of a kind
        elif (rank_of_hand == 0):
            if (number_of_jokers > 0):
                cards = '2' + cards
            else:
                cards = '4' + cards
        # Two pair
        elif (rank_of_hand == -1):
            if(number_of_jokers > 1):
                cards = '2' + cards
            elif (number_of_jokers > 0):
                cards = '3' + cards
            else:
                cards = '5' + cards
        # One pair
        elif (rank_of_hand == -2):
            if (number_of_jokers > 0):
                cards = '4' + cards
            else:
                cards = '6' + cards
        # High value
        elif (number_of_jokers > 0):
            cards = '6' + cards
        else:
            cards = '7' + cards
        return cards

    def solve(self, part_2: bool) -> None:
        start_time = time.time()
        hands = self.parse_hands(part_2)
        hands.sort(key=self.value_hand, reverse=True)
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
