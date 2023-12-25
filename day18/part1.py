import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    area = set()
    r, c = 0, 0
    left, right, top, bottom = float("inf"), -float("inf"), float("inf"), -float("inf")
    for line in input_text.splitlines():
        d, n_s, _ = line.split()
        n = int(n_s)
        if d == "R":
            dr, dc = 0, 1
        elif d == "L":
            dr, dc = 0, -1
        elif d == "U":
            dr, dc = -1, 0
        else:
            dr, dc = 1, 0
        for _ in range(n):
            r, c = r + dr, c + dc
            area.add((r, c))
        top = min(top, r)
        bottom = max(bottom, r)
        left = min(left, c)
        right = max(right, c)

    top = top - 1
    left = left - 1
    right = right + 1
    bottom = bottom + 1

    outside = area.copy()
    to_check = []
    to_check.append((top, left))
    while to_check:
        next_to_check = []
        for r, c in to_check:
            block = set()
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    next_r, next_c = r + dr, c + dc
                    if (
                        (top <= next_r <= bottom)
                        and left <= next_c <= right
                        and (next_r, next_c) not in outside
                    ):
                        outside.add((next_r, next_c))
                        next_to_check.append((next_r, next_c))
        to_check = next_to_check

    return (bottom - top + 1) * (right - left + 1) - len(outside) + len(area)


example = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

example_answer = 62


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
