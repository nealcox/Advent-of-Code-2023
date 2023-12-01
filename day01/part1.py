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

    answer = 0
    for line in input_text.split("\n"):
        digits = re.findall(r"(\d)", line)
        i = 10 * int(digits[0]) + int(digits[-1])
        answer += i

    return answer


example = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

example_answer = 142


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
