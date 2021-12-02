import sys

def process_line(l):
    return l

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f]

def part1(data):
    return None

def part2(data):
    return None

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))