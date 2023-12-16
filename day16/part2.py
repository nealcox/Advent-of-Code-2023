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

    nums_energised = set()
    given = input_text.splitlines()
    height = len(given)
    width = len(given[-1])
    for c in range(width):
        beam = (-1, c, "d")
        nums_energised.add(get_num_energised(beam, given, height, width))
        beam = (height, c, "u")
        nums_energised.add(get_num_energised(beam, given, height, width))
    for r in range(height):
        beam = (r, -1, "r")
        nums_energised.add(get_num_energised(beam, given, height, width))
        beam = (r, width, "l")
        nums_energised.add(get_num_energised(beam, given, height, width))

    return max(nums_energised)


def get_num_energised(beam, given, height, width):

    slash = {"r": "u", "l": "d", "u": "r", "d": "l"}  # /
    backslash = {"r": "d", "l": "u", "u": "l", "d": "r"}  # \
    seen = set()
    beams = set()
    beams.add(beam)
    while beams:
        next_beams = set()
        for r, c, d in beams:
            if d == "r":
                c += 1
            elif d == "l":
                c -= 1
            elif d == "u":
                r -= 1
            elif d == "d":
                r += 1
            if r >= 0 and r < height and c >= 0 and c < width:
                char = given[r][c]
                if char == "/":
                    next_beams.add((r, c, slash[d]))
                elif char == "\\":
                    next_beams.add((r, c, backslash[d]))
                elif char == "|" and d in "rl":
                    next_beams.add((r, c, "u"))
                    next_beams.add((r, c, "d"))
                elif char == "-" and d in "ud":
                    next_beams.add((r, c, "r"))
                    next_beams.add((r, c, "l"))
                else:
                    next_beams.add((r, c, d))
        beams = next_beams - seen
        seen |= beams

    energised = set()
    for r, c, d in seen:
        energised.add((r, c))

    return len(energised)


with open("test_input.txt") as f:
    example = f.read().strip()

example_answer = 51


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
