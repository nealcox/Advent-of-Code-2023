import re
import sys
from functools import cache


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    answer = 0
    for line in input_text.splitlines():
        pattern, nums_s = line.split()
        # Unfold
        pattern = (
            pattern + "?" + pattern + "?" + pattern + "?" + pattern + "?" + pattern
        )
        nums_s = nums_s + "," + nums_s + "," + nums_s + "," + nums_s + "," + nums_s
        nums = tuple(int(i) for i in re.findall(r"(\d+)", nums_s))
        ans = arrangements(pattern.strip("."), nums)
        answer += ans

    return answer


@cache
def arrangements(pattern, nums):
    # Can remove any leading/ trailing "."
    pattern = pattern.strip(".")

    # Base cases
    if not nums:
        if "#" in pattern:
            return 0  # We have "#"s left vut nothing to match them with
        else:
            return 1  # Any "?"s must be "."s fo only one combination
    elif not pattern:
        return 0  # We have numbers left but nothing to match them with

    # Non base cases
    if pattern[0] == "#":
        # pattern starts with a #, so must fit first number
        if len(pattern) < nums[0]:
            return 0
        matched = pattern[: nums[0]]
        if "." in matched:
            return 0  # Cannot fit first bit
        elif len(pattern) == nums[0]:
            if len(nums) == 1:
                return 1
            else:
                return 0
        elif pattern[nums[0]] == "#":
            return 0  # Cannot fit first bit in before the first "." or too long
        else:
            return arrangements(pattern[nums[0] + 1 :], nums[1:])

    if pattern[0] == "?":
        ans = 0
        while pattern and pattern[0] == "?":
            pattern = pattern[1:]
            ans += arrangements("#" + pattern, nums)
        ans += arrangements(pattern.strip(), nums)
        return ans

    raise ValueError(f"Unknown starting character in {pattern}")


example = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

example_answer = 525152


def test_example():
    assert calculate(example) == example_answer


example1 = "???.### 1,1,3"
example2 = ".??..??...?##. 1,1,3"
example3 = "?#?#?#?#?#?#?#? 1,3,1,6"
example4 = "????.#...#... 4,1,1"
example5 = "????.######..#####. 1,6,5"
example6 = "?###???????? 3,2,1"

example_answer1 = 1
example_answer2 = 16384
example_answer3 = 1
example_answer4 = 16
example_answer5 = 2500
example_answer6 = 506250


def test_example1():
    assert calculate(example1) == example_answer1


def test_example2():
    assert calculate(example2) == example_answer2


def test_example3():
    assert calculate(example3) == example_answer3


def test_example4():
    assert calculate(example4) == example_answer4


def test_example5():
    assert calculate(example5) == example_answer5


def test_example6():
    assert calculate(example6) == example_answer6


if __name__ == "__main__":
    exit(main())
