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

    answer = float("inf")
    directions = {"h": (("<", 0, -1), (">", 0, 1)), "v": (("^", -1, 0), ("v", 1, 0))}
    minima = defaultdict(lambda: float("inf"))

    area, height, width = get_map(input_text)
    # state: row, col which way to move
    # Cannot turn 180 degrees, so horizontal move must be followed by a
    # vertical move and vice versa. At each point, generate the fourteen possible
    # next positions
    state1 = (0, 0, "h")
    state2 = (0, 0, "v")
    minima[state1] = 0
    minima[state2] = 0
    to_check = []
    to_check.append(state1)
    to_check.append(state2)
    while to_check:
        next_to_check = []
        for state in to_check:
            row, col, direction = state
            if direction == "h":
                next_direction = "v"
            else:
                next_direction = "h"
            for d, dr, dc in directions[direction]:
                distance = 1
                next_row, next_col = row, col
                next_loss = minima[state]
                while distance < 4:  # Move mandatory distance of 4
                    # first item of next loop should be
                    # a distance of 4
                    distance += 1
                    next_row, next_col = next_row + dr, next_col + dc
                    next_loss = next_loss + area[next_row, next_col]
                while distance < 11:  # Move rest of distance
                    distance += 1
                    next_row, next_col = next_row + dr, next_col + dc
                    next_state = (next_row, next_col, next_direction)
                    next_loss = next_loss + area[next_row, next_col]
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and next_loss < minima[next_state]
                    ):
                        minima[next_state] = next_loss
                        if next_state not in next_to_check:
                            next_to_check.append(next_state)
                        if (next_row, next_col) == (height - 1, width - 1):
                            answer = min(answer, next_loss)
        to_check = next_to_check

    return answer


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


example = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

example_answer = 94


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
