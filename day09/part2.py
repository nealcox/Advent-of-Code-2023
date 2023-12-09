import sys
from collections import Counter


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    max_order = -1
    for line in input_text.splitlines():
        nums = [int(i) for i in line.split()]
        order = 0
        to_add = nums[0]
        while True:
            diffs = []
            order += 1
            for i, num1 in enumerate(nums[:-1]):
                num2= nums[i+1]
                diffs.append(num2 - num1)
            to_add += diffs[0] * (-1)**order
            if len(Counter(diffs)) == 1:
                break
            nums = diffs
        answer += to_add

    return answer


example = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

example_answer = 2


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
