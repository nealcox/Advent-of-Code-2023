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
    lines = parse(input_text)
    height = len(lines)
    width = len(lines[0])

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
            has_symbol = False
            for c in above:
                if c != "." and (not c.isdigit()):
                    has_symbol = True
                    break
            if not has_symbol:
                for c in below:
                    if c != "." and (not c.isdigit()):
                        has_symbol = True
                        break
            if s > 0:
                if line[s] != "." and (not c.isdigit()):
                    has_symbol = True
            if e < width:
                if line[e - 1] != "." and (not c.isdigit()):
                    has_symbol = True
            if has_symbol:
                answer += int(m.group(0))
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

example_answer = 4361


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
