import sys

def process_line(l):
    parts = l.split(' ')
    direction = parts[0]
    steps = int(parts[1])
    if direction == 'forward':
        return [steps, 0]
    if direction == 'down':
        return [0, steps]
    if direction == 'up':
        return [0, -steps]

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f]

def part1(data):
    x = sum([parts[0] for parts in data])
    y = sum([parts[1] for parts in data])
    return x * y

def part2(data):
    start = [0, 0]
    aim = 0
    for parts in data:
        aim += parts[1]
        start = [start[i] + parts[0] * pow(aim, i) for i in range(2)]
    return start[0] * start[1]

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))