import sys


def main():
    filename = "input.txt"
    to_remove = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        to_remove = sys.argv[2:]
    with open(filename) as f:
        input_text = f.read().strip()
    answer = calculate(input_text, to_remove)
    if answer:
        print(f"Answer: {answer}")


def calculate(input_text, to_remove):
    nodes = set()
    connections = defaultdict(set)
    single_connections = set()
    for line in input_text.splitlines():
        node_from, nodes_to = line.split(":")
        nodes.add(node_from)
        for node in nodes_to.strip().split():
            nodes.add(node)
            connections[node_from].add(node)
            connections[node].add(node_from)
            single_connections.add((node_from, node))

    if not to_remove:
        # Print the connections and use graphviz / dot to create the graph
        # of connections. The three important connections are then obvious
        #
        print("digraph {")
        for n1, n2 in single_connections:
            print(f'{n1} -> {n2} [label="{n1} {n2}" tooltip="{n1} {n2}" dir=both]')
        print("}")
        return
    # we get:
    #     ddc gqm
    #     dgt tnz
    #     kzh rks
    # so need to run
    # python part1.py input.txt ddc gqm dgt tnz kzh rks

    connections[to_remove[0]].remove(to_remove[1])
    connections[to_remove[1]].remove(to_remove[0])
    connections[to_remove[2]].remove(to_remove[3])
    connections[to_remove[3]].remove(to_remove[2])
    connections[to_remove[4]].remove(to_remove[5])
    connections[to_remove[5]].remove(to_remove[4])

    # Start from a random node, use variable node from above
    # See how many nodes we can get to, the two parts are
    # then what we can get to then all the other nodes
    seen = set()
    seen.add(node)
    to_check = []
    to_check.append(node)
    while to_check:
        next_to_check = set()
        for node_from in to_check:
            for node_to in connections[node_from]:
                if node_to not in seen:
                    seen.add(node_to)
                    next_to_check.add(node_to)
        to_check = next_to_check

    return len(seen) * (len(nodes) - len(seen))


example = """\
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

example_answer = 54


def test_example():
    assert (
        calculate(example, ["hfx", "pzl", "bvb", "cmg", "nvd", "jqt"]) == example_answer
    )


if __name__ == "__main__":
    exit(main())
