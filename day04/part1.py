import re
import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    for line in input_text.split("\n"):
        first, second = line.split("|")
        
        winning_nums = set([int(i) for i in re.findall(r"(-?\d+)", first)][1:])
        my_nums = set([int(i) for i in re.findall(r"(-?\d+)", second)])
        in_common = len(winning_nums & my_nums)
        if in_common:
            points = 2 ** (in_common - 1)
        else:
            points = 0
        answer += points

    return answer


example = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

example_answer = 13


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
