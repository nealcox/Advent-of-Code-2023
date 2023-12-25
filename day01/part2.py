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
    subs = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "4"),
        ("five", "5e"),
        ("six", "6"),
        ("seven", "7n"),
        ("eight", "e8t"),
        ("nine", "n9e"),
    ]
    for sub in subs:
        p = re.compile(sub[0])
        input_text = p.sub(sub[1], input_text)

    answer = 0
    for line in input_text.split("\n"):
        digits = re.findall(r"(\d)", line)
        i = 10 * int(digits[0]) + int(digits[-1])
        answer += i

    return answer


example = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

example_answer = 281


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
