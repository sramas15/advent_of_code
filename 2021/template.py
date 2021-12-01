import sys

def parse(fn):
    with open(fn) as f:
        return [l for l in f]

def part1(data):
    print("Part 1")

def part2(data):
    print("Part 2")

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))