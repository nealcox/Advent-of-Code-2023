import sys
from difflib import SequenceMatcher

##########################################


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0
    for pattern in input_text.split("\n\n"):
        lines = pattern.splitlines()
        answer += get_reflex(lines)

    return answer


def get_reflex(pattern):
    # Horizontal reflection

    for i in range(len(pattern) - 1):
        if str_diffs(pattern[i], pattern[i + 1]) < 2:  # Possible reflection
            total_diffs = 0
            num_reflected = min(i + 1, len(pattern) - i - 1)

            for j in range(num_reflected):
                diffs = str_diffs(pattern[i - j], pattern[i + 1 + j])
                total_diffs += str_diffs(pattern[i - j], pattern[i + 1 + j])
                print(f"total_diffs: {total_diffs}")
                if total_diffs > 1:
                    break
            if total_diffs == 1:
                return 100 * (i + 1)
    # Vertical reflection
    transposed = []
    for j in range(len(pattern[0])):
        transposed.append("".join(pattern[i][j] for i in range(len(pattern))))

    return int(get_reflex(transposed) / 100)


def str_diffs(s1, s2):
    return sum(0 if c1 == c2 else 1 for c1, c2 in zip(s1, s2))


example = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

example_answer = 400


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
