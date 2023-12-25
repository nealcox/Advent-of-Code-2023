import re
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
    given = get_re(input_text)
    for game_id, shown in given:
        min_red = 0
        min_green = 0
        min_blue = 0
        print(game_id, shown)
        for r, g, b in shown:
            min_red = max(min_red, r)
            min_green = max(min_green, g)
            min_blue = max(min_blue, b)
        print(min_red * min_green * min_blue)
        answer += min_red * min_green * min_blue

    return answer


def get_re(s):
    p_red = re.compile(r"(\d+) red")
    p_green = re.compile(r"(\d+) green")
    p_blue = re.compile(r"(\d+) blue")
    q = re.compile(r"(\d+)")
    r = re.compile(r":|;")

    given = []
    for line in s.split("\n"):
        parts = r.split(line)
        game_id = int(q.search(parts[0]).group())
        shown = []
        for cube_set in parts[1:]:
            if "red" in cube_set:
                num_red = int(p_red.search(cube_set).group(1))
            else:
                num_red = 0
            if "green" in cube_set:
                num_green = int(p_green.search(cube_set).group(1))
            else:
                num_green = 0
            if "blue" in cube_set:
                num_blue = int(p_blue.search(cube_set).group(1))
            else:
                num_blue = 0
            shown.append((num_red, num_green, num_blue))
        given.append((game_id, shown))
    return given


example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

example_answer = 2286


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
