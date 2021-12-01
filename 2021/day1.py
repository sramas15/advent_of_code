import sys

def preprocess(file_path):
    with open(file_path) as f:
        return [int(l.strip()) for l in f]

def part1(processed):
    num_increases = 0
    m = len(processed)
    last = processed[0]
    for i in range(1, m):
        cur = processed[i]
        if cur > last:
            num_increases += 1
        last = cur
    return num_increases


def part2(processed):
    num_increases = 0
    m = len(processed)
    last = sum([processed[i] for i in range(3)])
    for i in range(1, m):
        cur = sum([processed[j] if j < m else 0 for j in range(i, i + 3)])
        if cur > last:
            num_increases += 1
        last = cur
    return num_increases

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print("Please provide a file argument")
    else:
        processed = preprocess(sys.argv[1])
        print(part1(processed))
        print(part2(processed))