import re
import sys
from collections import defaultdict


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0
    seen = set()
    area, height, width = get_map(input_text)
    for point, char in area.items():
        if char == "S":
            seen.add(point)
            points = (point, point)

            r, c = point
            if area[r, c + 1] in "7-J" and area[r + 1, c] in "J|L":
                area[point] = "F"
            elif area[r, c - 1] in "FL-" and area[r + 1, c] in "J|L":
                area[point] = "7"
            else:
                raise ValueError("Need more start position analysis")
    while True:
        answer += 1
        next_points = set()
        for r, c in points:
            char = area[r, c]
            up = (r - 1, c)
            down = (r + 1, c)
            left = (r, c - 1)
            right = (r, c + 1)
            if char in "|LJ" and up not in seen and area[up] in "F7|":
                next_points.add(up)
                seen.add(up)
            if char in "|F7" and down not in seen and area[down] in "L|J":
                next_points.add(down)
                seen.add(down)
            if char in "-J7" and left not in seen and area[left] in "FL-":
                next_points.add(left)
                seen.add(left)
            if char in "-LF" and right not in seen and area[right] in "J7-":
                next_points.add(right)
                seen.add(right)
        if len(next_points) == 1:
            break
        else:
            assert len(next_points) == 2
            points = next_points
    return answer


def get_map(s):
    area = defaultdict(lambda: ".")

    lines = s.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            area[r, c] = char
    given = (area, height, width)
    return given


example = """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

example_answer = 8


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
