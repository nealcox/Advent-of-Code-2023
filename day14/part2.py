import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    cycles_to_do = 1000000000
    answer = 0
    seen = {}
    given = input_text.splitlines()
    height = len(given)
    width = len(given[0])
    fixed_rocks = set()
    rolling_rocks = set()
    seen = {}
    for r, line in enumerate(given):
        for c, char in enumerate(line):
            if line[c] == "O":
                rolling_rocks.add((r, c))
            elif line[c] == "#":
                fixed_rocks.add((r, c))

    cycles_done = 0
    period = None
    while cycles_done < cycles_to_do:
        if period:
            number_of_periods = (cycles_to_do - cycles_done) // period
            cycles_done += period * number_of_periods
        rolling_rocks = tilt_north(rolling_rocks, fixed_rocks, height, width)
        rolling_rocks = tilt_west(rolling_rocks, fixed_rocks, height, width)
        rolling_rocks = tilt_south(rolling_rocks, fixed_rocks, height, width)
        rolling_rocks = tilt_east(rolling_rocks, fixed_rocks, height, width)
        cycles_done += 1
        rolling_rocks_f = frozenset(rolling_rocks)
        if not period and rolling_rocks_f in seen:
            period = cycles_done - seen[rolling_rocks_f]
        else:
            seen[frozenset(rolling_rocks_f)] = cycles_done

    for r, _ in rolling_rocks:
        answer += height - r
    return answer


def tilt_north(rolling_rocks, fixed_rocks, height, width):
    next_rolling_rocks = set()
    for c in range(width):
        resting_row = 0
        r = 0
        while r < height:
            if (r, c) in fixed_rocks:
                resting_row = r
                while resting_row < height and (resting_row, c) in fixed_rocks:
                    resting_row += 1
            elif (r, c) in rolling_rocks:
                next_rolling_rocks.add((resting_row, c))
                resting_row += 1
                while resting_row < height and (resting_row, c) in fixed_rocks:
                    resting_row += 1
            r += 1
    return next_rolling_rocks


def tilt_west(rolling_rocks, fixed_rocks, height, width):
    next_rolling_rocks = set()
    for r in range(height):
        resting_col = 0
        c = 0
        while c < width:
            if (r, c) in fixed_rocks:
                resting_col = c
                while resting_col < width and (r, resting_col) in fixed_rocks:
                    resting_col += 1
            elif (r, c) in rolling_rocks:
                next_rolling_rocks.add((r, resting_col))
                resting_col += 1
                while resting_col < width and (r, resting_col) in fixed_rocks:
                    resting_col += 1
            c += 1
    return next_rolling_rocks


def tilt_south(rolling_rocks, fixed_rocks, height, width):
    next_rolling_rocks = set()
    for c in range(width):
        resting_row = height - 1
        r = height - 1
        while r > -1:
            if (r, c) in fixed_rocks:
                resting_row = r
                while resting_row > -1 and (resting_row, c) in fixed_rocks:
                    resting_row -= 1
            elif (r, c) in rolling_rocks:
                next_rolling_rocks.add((resting_row, c))
                resting_row -= 1
                while resting_row > -1 and (resting_row, c) in fixed_rocks:
                    resting_row -= 1
            r -= 1
    return next_rolling_rocks


def tilt_east(rolling_rocks, fixed_rocks, height, width):
    next_rolling_rocks = set()
    for r in range(height):
        resting_col = width - 1
        c = width - 1
        while c > -1:
            if (r, c) in fixed_rocks:
                resting_col = c
                while resting_col > -1 and (r, resting_col) in fixed_rocks:
                    resting_col -= 1
            elif (r, c) in rolling_rocks:
                next_rolling_rocks.add((r, resting_col))
                resting_col -= 1
                while resting_col > -1 and (r, resting_col) in fixed_rocks:
                    resting_col -= 1
            c -= 1
    return next_rolling_rocks


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

example_answer = 64


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
