import sys

def process_line(l):
    return [int(i) for i in l.split(',')]

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f][0]

def get_fib_to_val(val):
    start = 0
    m = {}
    for i in range(0, val + 1):
        start += i
        m[i] = start
    return m

def find_cost(data, num):
    return sum([abs(d - num) for d in data])

def find_cost2(data, num, fib):
    return sum([fib[abs(d - num)] for d in data])

def compute(data, lam):
    start = data[0]
    end = data[-1]
    while start <= end:
        mid = int((start + end)/2)
        m_cost = lam(data, mid)
        if lam(data, mid+1) < m_cost:
            start = mid + 1
        elif lam(data, mid-1) < m_cost:
            end = mid - 1
        else:
            return m_cost

def part1(data):
    return compute(data, lambda x, y: find_cost(x, y))

def part2(data):
    fib = get_fib_to_val(data[-1])
    return compute(data, lambda x, y: find_cost2(x, y, fib))

if __name__ == "__main__":
    data = sorted(parse(sys.argv[1]))
    print(part1(data))
    print(part2(data))