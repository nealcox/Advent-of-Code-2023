import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    given = input_text.split("\n\n")
    seedinfo = [int(i) for i in given[0].split(" ")[1:]]
    it = iter(seedinfo)
    seed_ranges = []
    for x in it:
        seed_ranges.append((x, next(it)))

    mapped = []
    for seed, seed_range in seed_ranges:
        max_seed = seed + seed_range - 1

        while seed < max_seed:
            test_number = seed
            valid_range = seed_range
            for mapping in given[1:]:
                test_number, valid_range_for_mapping = do_mapping(
                    test_number, mapping, valid_range
                )
                valid_range = min(valid_range, valid_range_for_mapping)
            mapped.append(test_number)
            seed += valid_range

    return min(mapped)


def do_mapping(test_number, mapping, valid_range):
    mapping = mapping.splitlines()
    out = None
    for line in mapping[1:]:
        mapped_to, mapped_from, max_index = (int(i) for i in line.split(" "))
        if test_number >= mapped_from and (test_number - mapped_from) < max_index:
            out = test_number - mapped_from + mapped_to
            valid_range = min(valid_range, max_index - test_number + mapped_from)
            break
    if not out:
        out = test_number
        for line in mapping[1:]:
            mapped_to, mapped_from, max_index = (int(i) for i in line.split(" "))
            if test_number < mapped_from:
                valid_range = min(valid_range, mapped_from - test_number)

    return out, valid_range


example = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

example_answer = 46


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
