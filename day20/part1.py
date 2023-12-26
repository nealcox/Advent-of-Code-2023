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
    TOTAL_PUSHES = 1000
    type_indicators = {"b": "broadcaster", "%": "flipflop", "&": "conjunction"}
    flipflops = defaultdict(lambda: "off")
    conjunctions = {}

    pulses = {"low": 0, "high": 0}
    system = defaultdict(lambda: (None, []))
    # Name: (type, [dests])
    for module in input_text.splitlines():
        first, rest = module.split(" -> ")
        type_indicator = first[0]
        module_type = type_indicators[type_indicator]
        if first == "broadcaster":
            name = "broadcaster"
        else:
            name = first[1:]
        dests = rest.split(", ")
        system[name] = (module_type, dests)
        if module_type == "conjunction":
            conjunctions[name] = {}
    for name, (module_type, dests) in system.items():
        for d in dests:
            if d in conjunctions:
                conjunctions[d][name] = "off"

    for push in range(TOTAL_PUSHES):
        to_process = [("button", "low", "broadcaster")]
        pulses["low"] += 1
        while to_process:
            sender, pulse, receiver = to_process.pop(0)
            module_type, dests = system[receiver]
            if module_type == "broadcaster":
                for d in dests:
                    to_process.append(("broadcaster", pulse, d))
                    pulses[pulse] += 1
            elif module_type == "flipflop":
                if pulse == "low":
                    if flipflops[receiver] == "off":
                        flipflops[receiver] = "on"
                        for d in dests:
                            to_process.append((receiver, "high", d))
                            pulses["high"] += 1
                    else:
                        flipflops[receiver] = "off"
                        for d in dests:
                            to_process.append((receiver, "low", d))
                            pulses["low"] += 1
            elif module_type == "conjunction":
                conjunctions[receiver][sender] = pulse
                if pulse == "high" and len(set(conjunctions[receiver].values())) == 1:
                    # One high and all the same -> all high
                    out_pulse = "low"
                else:
                    out_pulse = "high"
                for d in dests:
                    to_process.append((receiver, out_pulse, d))
                    pulses[out_pulse] += 1

    return pulses["low"] * pulses["high"]


example1 = """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

example2 = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

example_answer1 = 32000000
example_answer2 = 11687500


def test_example1():
    assert calculate(example1) == example_answer1


def test_example2():
    assert calculate(example2) == example_answer2


if __name__ == "__main__":
    exit(main())
