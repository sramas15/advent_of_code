import sys

def parse(file_path):
    with open(file_path) as f:
        return [int(l.strip()) for l in f]

def get_num_increases(data, lam):
    num_increases = 0
    m = len(data)
    last = lam(0, m, data)
    for i in range(1, m):
        cur = lam(i, m, data)
        if cur > last:
            num_increases += 1
        last = cur
    return num_increases

def part1(data):
    p1 = lambda i, m, data: data[i]
    return get_num_increases(data, p1)


def part2(data):
    p2 = lambda i, m, data: sum([data[j] if j < m else 0 for j in range(i, i + 3)])
    return get_num_increases(data, p2)

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))