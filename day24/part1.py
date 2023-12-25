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


def calculate(input_text, min_xy=200000000000000, max_xy=400000000000000):
    r = re.compile(r"(-?\d+)")

    answer = 0
    hailstones = []
    for l in input_text.splitlines():
        stone = []
        for i in r.findall(l):
            stone.append(int(i))
        hailstones.append(stone)

    intersections = set()
    for first, stone1 in enumerate(hailstones[:-1]):
        x1, y1, _, vx1, vy1, _ = stone1
        # A line defined by a point, (x0, y0) and a slope (vx,vy
        #
        # At time t is at position
        # (x, y) = (x0 + t*vx, y0 + t(vy)
        # x = x0 + t * vx -> t = (x - x0) / vx
        # y = y0 + t * vy
        #   = y0 + vy * (x - x0) / vx
        #   = x *vy/vx + y0 -x0 * vy / vx
        for second, stone2 in enumerate(hailstones[first + 1 :]):
            x2, y2, _, vx2, vy2, _ = stone2
            if not_parallel(vx1, vy1, vx2, vy2):
                # x & y equal for each stone, use formula for y to solve for common x
                #  x *vy1/vx1 + y1 - x1*vy1/vx1 = x *vy2/vx2 + y2 - x2*vy2/vx2
                #  x * (vy1/vx1 - vy2/vx2) = y2 - x2*vy2/vx2 -y1 + x1*vy1/vx1
                #  x = (y2 - x2*vy2/vx2 -y1 + x1*vy1/vx1) / ( vy1/vx1 - vy2/vx2)

                # Special case if either is vertical, plg x value into other line
                if vx1 == 0:
                    x = x1
                    y = x * vy2 / vx2 + y2 - x2 * vy2 / vx2
                elif vx2 == 0:
                    x = x2
                    y = x * vy1 / vx1 + y1 - x1 * vy1 / vx1
                else:
                    x = (y2 - x2 * vy2 / vx2 - y1 + x1 * vy1 / vx1) / (
                        vy1 / vx1 - vy2 / vx2
                    )
                    y = x * vy2 / vx2 + y2 - x2 * vy2 / vx2

                # Look at when paths cross for each stone
                if vx1 != 0:
                    t1 = (x - x1) / vx1
                else:
                    t1 = (y - y1) / vy1
                if vx2 != 0:
                    t2 = (x - x2) / vx2
                else:
                    t2 = (y - y2) / vy2

                if (
                    min_xy <= x <= max_xy
                    and min_xy <= y <= max_xy
                    and t1 >= 0
                    and t2 >= 0
                ):
                    intersections.add((first, second))
    return len(intersections)


def not_parallel(vx1, vy1, vx2, vy2):
    return vx1 * vy2 != vx2 * vy1


example = """\
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

example_answer = 2


def test_example():
    assert calculate(example, 7, 27) == example_answer


if __name__ == "__main__":
    exit(main())
