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
    given = parse(input_text)
    print(given)

    return answer


def parse(s):
    given = None
    # given = partlines(s)
    # given = get_one_int_per_line(s)
    # given = get_re(s)
    # given = get_all_ints(s)
    given = get_map(s)  # given is tuple (area_map, height, width)
    return given


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.strip()
        given.append(line)
    return given


def get_map(s):
    area = defaultdict(lambda: float("inf"))

    lines = s.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            area[r, c] = int(char)
    given = (area, height, width)
    return given


def get_one_int_per_line(s):
    ints = []
    for line in s.split("\n"):
        ints.append(int(line))
    return ints


def get_re(s):
    given = []
    r = re.compile(r"(\w+) (\d+)")
    for m in r.findall(s):
        given.append((m[0], int(m[1])))
    return given


def get_all_ints(s):
    return (int(i) for i in re.findall(r"(-?\d+)", s))


example = """\
X"""

example_answer = X


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
