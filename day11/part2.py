import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    galaxies = []
    rows = input_text.splitlines()
    blank_rows = set()
    for i, r in enumerate(rows):
        if len(set(r)) == 1:
            blank_rows.add(i)

    blank_cols = set()
    for c in range(len(rows[0])):
        blank = True
        for r, row in enumerate(rows):
            if row[c] != ".":
                galaxies.append((r, c))
                blank = False
        if blank:
            blank_cols.add(c)

    shortest_paths = []
    for g, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[g + 1 :]:
            r1, c1 = galaxy1
            r2, c2 = galaxy2
            if r2 < r1:
                r1, r2 = r2, r1
            if c2 < c1:
                c1, c2 = c2, c1
            path_length = r2 - r1 + c2 - c1
            for r in range(r1, r2):
                if r in blank_rows:
                    path_length += 1000000 - 1
            for c in range(c1, c2):
                if c in blank_cols:
                    path_length += 1000000 - 1
            shortest_paths.append(path_length)

    return sum(shortest_paths)


if __name__ == "__main__":
    exit(main())
