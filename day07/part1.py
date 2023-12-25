import re
import sys
from collections import Counter


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6


def calculate(input_text):
    answer = 0
    hands = []
    for line in input_text.splitlines():
        hand, bid = line.split(" ")
        bid = int(bid)
        hands.append((hand, bid))

    by_type = [[], [], [], [], [], [], []]
    # rank from low to high
    for hand, bid in hands:
        card_counts = Counter(hand)
        s = max(card_counts.values())
        if s == 1:  # High card
            by_type[HIGH_CARD].append((hand, bid))
        elif s == 2:  # Pairs
            num_pairs = Counter(card_counts.values())[2]
            if num_pairs == 1:
                by_type[ONE_PAIR].append((hand, bid))  # One Pair
            else:
                by_type[TWO_PAIR].append((hand, bid))  # Two pairs
        elif s == 3 and 2 not in card_counts.values():  # Three of a kind
            by_type[THREE_OF_A_KIND].append((hand, bid))
        elif s == 3:  # Full House
            by_type[FULL_HOUSE].append((hand, bid))
        elif s == 4:  # Four of a kind
            by_type[FOUR_OF_A_KIND].append((hand, bid))
        elif s == 5:  # Five of a kind
            by_type[FIVE_OF_A_KIND].append((hand, bid))
        else:
            raise ValueError(f"Cannot score {hand}")
    sorted_hands = []
    for hand_type in by_type:
        sorted_hands.append(sorted(hand_type, key=hand_value))

    all_hands = []
    for hand_type in sorted_hands:
        all_hands.extend(hand_type)

    for i, hand in enumerate(all_hands, start=1):
        answer += i * hand[1]

    return answer


def hand_value(s):
    cards = "AKQJT98765432"
    card_values = {}
    for c in cards:
        card_values[c] = 13 - cards.index(c)

    out = []
    for card in s[0]:
        out.append(card_values[card])
    return out


example = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

example_answer = 6440


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
