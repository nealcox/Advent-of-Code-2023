import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    lines = parse(input_text)
    height = len(lines)
    width = len(lines[0])

    gears = defaultdict(list)

    row = 0
    for row, line in enumerate(lines):
        above = "."
        below = "."
        for m in re.finditer(r"\d+", line):
            s = max(0, m.start() - 1)
            e = min(width, m.end() + 1)
            if row > 0:
                above = lines[row - 1][s:e]
            if row < height - 1:
                below = lines[row + 1][s:e]

            i = above.find("*")
            if i != -1:
                gear_row = row - 1
                gear_col = s + i
                gears[gear_row, gear_col].append(int(m.group(0)))
            i = below.find("*")
            if i != -1:
                gear_row = row + 1
                gear_col = s + i
                gears[gear_row, gear_col].append(int(m.group(0)))
            if line[s] == "*":
                gear_row = row
                gear_col = s
                gears[gear_row, gear_col].append(int(m.group(0)))
            if line[e - 1] == "*":
                gear_row = row
                gear_col = e - 1
                gears[gear_row, gear_col].append(int(m.group(0)))

    for l in gears.values():
        if len(l) == 2:
            answer += l[0] * l[1]

    return answer


def parse(s):
    given = []
    for line in s.split("\n"):
        line = line.strip()
        given.append(line)
    return given


example = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

example_answer = 467835


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
