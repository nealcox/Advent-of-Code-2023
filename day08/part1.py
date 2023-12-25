import re
import sys
from itertools import cycle


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    directions_s, mappings_s = input_text.split("\n\n")
    directions = cycle(directions_s)
    mappings = {}
    for line in mappings_s.splitlines():
        from_, l, r = re.findall(r"(\w+)", line)
        mappings[from_] = (l, r)
    location = "AAA"
    answer = 0
    for d in directions:
        if d == "L":
            location = mappings[location][0]
        else:
            location = mappings[location][1]
        answer += 1
        if location == "ZZZ":
            break

    return answer


example = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example_answer = 2

example2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

example_answer2 = 6


def test_example():
    assert calculate(example) == example_answer


def test_example2():
    assert calculate(example2) == example_answer2


if __name__ == "__main__":
    exit(main())
