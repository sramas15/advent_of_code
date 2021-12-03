import sys

def process_line(l):
    return [int(i) for i in l]

def parse(fn):
    with open(fn) as f:
        return [process_line(l.strip()) for l in f]

def get_num_from_bin(bits):
    rev = bits[::-1]
    num = 0
    for i in range(len(rev)):
        num += rev[i] * pow(2, i)
    return num

def part1(data):
    num_bits = len(data[0])
    half = int(len(data) / 2)
    gamma_bits = [1 if sum([r[i] for r in data]) > half else 0 for i in range(num_bits)]
    epsilon_bits = [1 if sum([r[i] for r in data]) <= half else 0 for i in range(num_bits)]
    return get_num_from_bin(gamma_bits) * get_num_from_bin(epsilon_bits)

def get_num_meet_criteria(data, lam):
    num_bits = len(data[0])
    for i in range(num_bits):
        data = filter(lambda row: lam(data, i, row[i]) , data)
        if len(data) == 1:
            return data[0]

def gas_matches(data, pos, val, val_to_match):
    half = int(len(data) / 2)
    num1s = sum([data[i][pos] for i in range(len(data))])
    if num1s * 2 == len(data):
        return val == val_to_match
    if num1s > half and val == val_to_match:
        return True
    if num1s <= half and val == abs(val_to_match - 1):
        return True
    return False

def part2(data):
    num1s = [sum([data[i][pos] for i in range(len(data))]) for pos in range(len(data[0]))]
    oxy = lambda x, y, z: gas_matches(x, y, z, 1)
    oxy_gen = get_num_from_bin(get_num_meet_criteria(data, oxy))
    co2 = lambda x, y, z: gas_matches(x, y, z, 0)
    co2_gen = get_num_from_bin(get_num_meet_criteria(data, co2))
    return oxy_gen * co2_gen

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))