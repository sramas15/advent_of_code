import sys

def parse(fn):
    with open(fn) as f:
        return [l for l in f]

def part1(data):
    return None

def part2(data):
    return None

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))