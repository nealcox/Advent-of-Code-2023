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
    given = input_text.splitlines()
    num_rows = len(given)
    for c in range(len(given[0])):
        resting_row = 0
        r = 0
        while r < num_rows:
            char = given[r][c]
            if char == "O":
                answer += num_rows - resting_row
                resting_row += 1
                while resting_row < num_rows and given[resting_row][c] == "#":
                    resting_row += 1
            elif char == "#":
                resting_row = r
                while resting_row < num_rows and given[resting_row][c] == "#":
                    resting_row += 1
            r += 1

    return answer


example = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

example_answer = 136


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
