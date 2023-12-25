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
    for pattern in input_text.split("\n\n"):
        lines = pattern.splitlines()
        answer += get_reflex(lines)

    return answer


def get_reflex(pattern):
    # Horizontal reflection

    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:  # Possible reflection
            num_reflected = min(i + 1, len(pattern) - i - 1)
            reflection = True
            for j in range(num_reflected):
                if pattern[i - j] != pattern[i + 1 + j]:
                    # not a reflection
                    reflection = False
            if reflection:
                return 100 * (i + 1)
    # Vertical reflection
    transposed = []
    for j in range(len(pattern[0])):
        transposed.append("".join(pattern[i][j] for i in range(len(pattern))))

    return int(get_reflex(transposed) / 100)


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

example_answer = 405


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
