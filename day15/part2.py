import sys
from collections import defaultdict


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    boxes = defaultdict(list)
    for s in input_text.split(","):
        if s[-1] == "-":
            label = s[:-1]
            boxnum = hash_(label) % 256
            for tpl in boxes[boxnum]:
                if tpl[0] == label:
                    boxes[boxnum].remove(tpl)
                    break
        elif "=" in s:
            label, focal_length_s = s.split("=")
            focal_length = int(focal_length_s)
            boxnum = hash_(label) % 256
            changed = False
            for i, tpl in enumerate(boxes[boxnum]):
                if tpl[0] == label:
                    boxes[boxnum][i] = (label, focal_length)
                    changed = True
            if not changed:
                boxes[boxnum].append((label, focal_length))

    answer = 0
    for b in range(256):
        for s, tpl in enumerate(boxes[b]):
            answer += (b + 1) * (s + 1) * tpl[1]

    return answer


def hash_(s):
    h = 0
    for i in range(len(s), 0, -1):
        h += ord(s[len(s) - i]) * (17**i)
    return h


example = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

example_answer = 145


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
