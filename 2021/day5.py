import sys

def process_line(l):
    parts = l.split(' -> ')
    coordA = [int(i.strip()) for i in parts[0].strip().split(',')]
    coordB = [int(i.strip()) for i in parts[1].strip().split(',')]
    return (coordA, coordB)

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f]

def find_dangerous_areas(data, include_diag):
    points = {}
    for coordA, coordB in data:
        if not include_diag and coordA[0] != coordB[0] and coordA[1] != coordB[1]:
            continue
        xInc = max([-1, min([1, coordB[0] - coordA[0]])])
        yInc = max([-1, min([1, coordB[1] - coordA[1]])])
        for i in range(max([abs(coordB[0] + xInc - coordA[0]), abs(coordB[1] + yInc - coordA[1])])):
            key = (coordA[0] + i * xInc, coordA[1] + i * yInc)
            if key not in points:
                points[key] = 0
            points[key] += 1
    return sum([1 if points[k] >= 2 else 0 for k in points])

def part1(data):
    return find_dangerous_areas(data, False)

def part2(data):
    return find_dangerous_areas(data, True)

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))