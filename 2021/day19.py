import sys
import itertools
import numpy as np

def rotations(array):
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx
            rotation_matrix[1, y] = sy
            rotation_matrix[2, z] = sz
            if np.linalg.det(rotation_matrix) == 1:
                yield [int(i) for i in list(np.matmul(rotation_matrix, array))]

def get_rotations_map(beacons):
    rotations_map = {}
    for point in beacons:
        rotations_map[str(point)] = list(rotations(point))
    return rotations_map

def add_points(x, y):
    return [x[i] + y[i] for i in range(3)]

def subtract_points(x, y):
    return [x[i] - y[i] for i in range(3)]

class Scanner:
    def __init__(self, beacons, id):
        self.beacons = beacons
        self.rotation = 0
        self.rotation_map = get_rotations_map(self.beacons)
        self.offset = [0, 0, 0]
        self.id = id

    def get_rotations(self):
        return range(24)

    def get_rotated_beacons_with_offset(self):
        return [add_points(self.rotation_map[str(k)][self.rotation], self.offset) for k in self.rotation_map]

    def set_rotation(self, val):
        assert val in self.get_rotations()
        self.rotation = val

    def set_offset(self, val):
        assert len(val) == 3
        self.offset = val

def get_set(l):
    return set([str(i) for i in l])

def does_match(fixed, current, num_overlap):
    num_points = len(current.beacons)
    fixed_points = fixed.get_rotated_beacons_with_offset()
    fixed_set = get_set(fixed_points)
    for r in current.get_rotations():
        current.set_offset([0, 0, 0])
        current.set_rotation(r)
        rotated_points = current.get_rotated_beacons_with_offset()
        for i in range(num_points - num_overlap + 1):
            current_point = rotated_points[i]
            for fixed_point in fixed_points:
                offset = subtract_points(fixed_point, current_point)
                current.set_offset(offset)
                current_set = get_set(current.get_rotated_beacons_with_offset())
                if len(fixed_set.intersection(current_set)) >= num_overlap:
                    return True
    return False

def algorithm(scanners, num_overlap):
    known = [scanners[0]] # All the scanners for which we know the offset
    added = [scanners[0]] # Scanners that we figured out the offset on in the last iteration
    rem = scanners[1:] # Scanners that we do not know the offset
    while len(rem) > 0:
        to_remove = [] # Scanners that we have figured out the offset for
        for i, scanner in enumerate(rem):
            for fixed in added: # We only need to check for matches in the scanners that were just added (so we don't do duplicate does_match calls)
                if does_match(fixed, scanner, num_overlap):
                    to_remove += [i]
                    break
        assert len(to_remove) > 0
        added = [rem[i] for i in to_remove]
        known += added
        rem = list(filter(None, [None if i in to_remove else rem[i] for i in range(len(rem))]))
    a = set()
    for m in known:
        a = a.union(get_set(m.get_rotated_beacons_with_offset()))
    return scanners, a

def process_line(l):
    return [int(i) for i in l.strip().split(',')]

def parse(fn):
    with open(fn) as f:
        scanners = []
        current = []
        for l in f:
            if len(l.strip()) == 0:
                if len(current) > 0:
                    scanners.append(Scanner(current, len(scanners)))
                    current = []
                continue
            current.append(process_line(l))
        if len(current) > 0:
            scanners.append(Scanner(current, len(scanners)))
    return scanners

def part1(beacons):
    return len(beacons)

def part2(scanners):
    return max([sum([abs(v) for v in subtract_points(scanners[i].offset, scanners[j].offset)]) for i in range(len(scanners)) for j in range(i + 1, len(scanners))])

if __name__ == "__main__":
    data = parse(sys.argv[1])
    scanners, beacons = algorithm(data, 12)
    print(part1(beacons))
    print(part2(scanners))
