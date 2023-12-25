import re
import sys
import z3


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    r = re.compile(r"(-?\d+)")

    answer = 0
    hailstones = []
    for l in input_text.splitlines():
        stone = []
        for i in r.findall(l):
            stone.append(int(i))
        hailstones.append(stone)

    solver = z3.Solver()

    rock_x = z3.Int("rock_x")
    rock_y = z3.Int("rock_y")
    rock_z = z3.Int("rock_z")
    rock_vx = z3.Int("rock_vx")
    rock_vy = z3.Int("rock_vy")
    rock_vz = z3.Int("rock_vz")

    for i, hailstone in enumerate(hailstones):
        time = z3.Int(f"t_{i}")
        solver.add(time >= 0)
        solver.add(rock_x + time * rock_vx == hailstone[0] + time * hailstone[3])
        solver.add(rock_y + time * rock_vy == hailstone[1] + time * hailstone[4])
        solver.add(rock_z + time * rock_vz == hailstone[2] + time * hailstone[5])

    assert solver.check() == z3.sat
    m = solver.model()
    return m[rock_x].as_long() + m[rock_y].as_long() + m[rock_z].as_long()


example = """\
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

example_answer = 47


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
