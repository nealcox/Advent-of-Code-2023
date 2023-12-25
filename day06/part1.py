import re
import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 1
    lines = input_text.splitlines()
    times = [int(i) for i in re.findall(r"(-?\d+)", lines[0])]
    dists = [int(i) for i in re.findall(r"(-?\d+)", lines[1])]
    races = zip(times, dists)
    for race in races:
        print(f"{race=}")
        time, dist = race
        # hold for time t, distance travelled  is (time - t) x t
        # (time**2)/4 -  ( (t - time/2)  ** 2 ) = -(  t ** 2 - t * time)
        # need -t**2 + time * t - dist > 0
        # so solve for equals 0 and valid for those between
        # use quadratic formaula with
        a, b, c = -1, time, -dist
        low = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
        high = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)

        low = int(low + 1)
        if int(high) == high:
            # Round number need to omit as would equal , not beat
            high -= 1
        high = int(high)

        wins = high - low + 1
        print(wins)
        answer *= wins
    return answer


example = """\
Time:      7  15   30
Distance:  9  40  200
"""

example_answer = 288


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
