import sys

def process_line(l):
    return [int(i) for i in l.strip().split(',')]

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f]

def num_produce(num, days_remaining, cache):
    key = (num, days_remaining) 
    if key not in cache:
        cache[key] = 1 + sum([num_produce(8, i, cache) for i in range(days_remaining - num - 1, -1, -7)])
    return cache[key]

def part1(data, cache):
    return sum([num_produce(d, 80, cache) for d in data])

def part2(data, cache):
    return sum([num_produce(d, 256, cache) for d in data])

if __name__ == "__main__":
    cache = {}
    data = parse(sys.argv[1])
    print(part1(data[0], cache))
    print(part2(data[0], cache))