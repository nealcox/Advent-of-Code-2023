import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    points = []
    lines = input_text.splitlines()

    r, c = 0, 0
    points.append((r, c))
    perimeter = 0

    for i, line in enumerate(lines):
        _, _, instruction = line.split()
        d = instruction[-2]
        n = int(instruction[2:7], 16)
        if d == "0":  # "R"
            c += n
        elif d == "2":  # "L"
            c -= n
        elif d == "3":  # "U"
            r -= n
        else:  #  "D"
            r += n
        perimeter += n
        points.append((r, c))

    # Calculate internal area (Shoelace theorem)
    # https://en.wikipedia.org/wiki/Shoelace_formula
    internal_area = 0
    for i, (r1, c1) in enumerate(points[:-1]):
        r2, c2 = points[i + 1]
        internal_area += r1 * c2 - c1 * r2
    internal_area = abs(internal_area) // 2

    # Points in side the area (Pick's Theorem)
    # https://en.wikipedia.org/wiki/Pick's_theorem
    # all points on perimeter are integer points
    internal_points = internal_area - perimeter // 2 + 1

    return internal_points + perimeter


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

example_answer = 952408144115


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
