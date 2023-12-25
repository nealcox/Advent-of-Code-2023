import re
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
    workflows_in, parts_in = input_text.split("\n\n")

    workflows = defaultdict(list)
    for workflow_in in workflows_in.splitlines():
        workflow = []
        name, rest = workflow_in.strip("}").split("{")
        rules = rest.split(",")
        for rule in rules[:-1]:
            cond, res = rule.split(":")
            workflows[name].append((cond, res))
        workflows[name].append(("True", rules[-1]))

    rule_range = ["in", 1, 4000, 1, 4000, 1, 4000, 1, 4000]
    rules_ranges = []
    rules_ranges.append(rule_range)
    lows = {"x": 1, "m": 3, "a": 5, "s": 7}
    highs = {"x": 2, "m": 4, "a": 6, "s": 8}
    accepted = []

    # start with [[ "in", 1, 4000, 1, 4000, 1, 4000, 1,4000 ]]
    # if "in" = in{s<1351:px,qqz}
    # get
    #             [[ "px",   1, 4000, 1, 4000, 1, 4000, 1,    1350 ],
    #              [ "qqz",  1, 4000, 1, 4000, 1, 4000, 1351, 4000 ]]

    # start with [[ "px", 1, 4000, 1, 4000, 1, 4000, 1,4000 ]]
    # if px{x<2006:qkq,m>2090:A,rfg}
    # get
    #             [[ "qkq",    1, 2005,    1, 4000, 1, 4000, 1,4000 ],
    #              [ "A",   2006, 4000, 2091, 4000, 1, 4000, 1,4000 ],
    #              [ "rfg", 2006, 4000,    1, 2090, 1, 4000, 1,4000 ]]
    while rules_ranges:
        next_ranges = []
        for rule_range in rules_ranges:
            rule_range = rule_range[:]
            w, x_low, x_high, m_low, m_high, a_low, a_high, s_low, s_high = rule_range
            for cond, res in workflows[w][:-1]:
                cat = cond[0]
                low, high = lows[cat], highs[cat]
                moreorless = cond[1]
                value = int(cond[2:])
                if moreorless == "<":
                    if rule_range[low] > value:
                        pass  # No possibilities
                    elif rule_range[high] < value:
                        next_ranges.append(rule_range[:])  # all possibilities
                        break
                    else:
                        old_high = rule_range[high]
                        rule_range[0] = res
                        rule_range[high] = value - 1
                        next_ranges.append(rule_range[:])
                        rule_range[high] = old_high
                        rule_range[low] = value
                elif moreorless == ">":
                    if rule_range[high] < value:
                        pass  # No possibilities
                    elif rule_range[low] > value:
                        next_ranges.append(rule_range[:])  # all possibilities
                        break
                    else:
                        old_low = rule_range[low]
                        rule_range[0] = res
                        rule_range[low] = value + 1
                        next_ranges.append(rule_range[:])
                        rule_range[low] = old_low
                        rule_range[high] = value
            rule_range[0] = workflows[w][-1][1]
            next_ranges.append(rule_range)
        rules_ranges = []
        for nr in next_ranges:
            if nr[0] == "A":
                accepted.append(nr)
            elif nr[0] != "R":
                rules_ranges.append(nr)

    answer = 0
    for a in accepted:
        w, x_low, x_high, m_low, m_high, a_low, a_high, s_low, s_high = a
        num = (
            (x_high - x_low + 1)
            * (m_high - m_low + 1)
            * (a_high - a_low + 1)
            * (s_high - s_low + 1)
        )
        answer += num

    return answer


example = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

example_answer = 167409079868000


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
