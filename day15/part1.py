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
    for s in input_text.split(","):
        answer += hash_(s) % 256

    return answer


def hash_(s):
    h = 0
    for i in range(len(s), 0, -1):
        h += ord(s[len(s) - i]) * (17**i)
    return h


example = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

example_answer = 1320


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
