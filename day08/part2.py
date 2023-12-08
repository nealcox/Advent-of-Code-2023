import re
import sys
from itertools import cycle
from math import lcm


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    # Takes too long to step through until end reached.
    # Instead, consider each starting location indiviually. Each one cycles,
    # so calculate each cycle length and then take LCM of all the cycles.

    directions_s, mappings_s = input_text.split("\n\n")
    directions = cycle(directions_s)
    mappings = {}
    for line in mappings_s.splitlines():
        from_, l, r = re.findall(r"(\w+)", line)
        mappings[from_] = (l, r)
    locations = []
    for loc in mappings:
        if loc[-1] == "A":
            locations.append(loc)
    cycle_lengths = []
    for loc in locations:
        cycle_length = 0
        for d in directions:
            if d == "L":
                loc = mappings[loc][0]
            else:
                loc = mappings[loc][1]
            cycle_length += 1
            if loc[-1] == "Z":
                cycle_lengths.append(cycle_length)
                break

    return lcm(*cycle_lengths)


example = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

example_answer = 6


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
