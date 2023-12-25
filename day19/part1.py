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

    changes_made = True
    while changes_made:
        changes_made = False
        to_delete = set()
        for workflow, rules in workflows.items():
            if len(rules) == 1:
                to_delete.add(workflow)
                changes_made = True
            elif rules[-2][1] == rules[-1][1]:
                workflows[workflow].pop(-2)
                changes_made = True
        next_workflows = {}
        for workflow, rules in workflows.items():
            if workflow not in to_delete:
                next_rules = [
                    (cond, res)
                    if res not in to_delete
                    else (cond, workflows[res][0][1])
                    for (cond, res) in rules
                ]
                next_workflows[workflow] = next_rules
        workflows = next_workflows

    answer = 0
    for part in parts_in.splitlines():
        x, m, a, s = (int(i) for i in re.findall(r"(\d+)", part))
        w = "in"
        while w not in "AR":
            for rule in workflows[w]:
                if eval(rule[0]):
                    w = rule[1]
                    break
        if w == "A":
            answer += x + m + a + s
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

example_answer = 19114


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
