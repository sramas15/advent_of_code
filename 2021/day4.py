import sys

class BingoBoard:
    def __init__(self, lines):
        self.lines = [[int(i) for i in filter(lambda x: x, l.strip().split(' '))] for l in lines]
        self.rows = [len(self.lines) for i in range(len(self.lines))]
        self.cols = [len(self.lines) for i in range(len(self.lines[0]))]
        self.last_num_called = None
        self.unmarked_sum = sum([val for r in self.lines for val in r])

    def call_number(self, number):
        self.last_num_called = number
        for i, row in enumerate(self.lines):
            for j, val in enumerate(row):
                if number == val:
                    self.rows[i] -= 1
                    self.cols[j] -= 1
                    self.unmarked_sum -= number

    def has_won(self):
        vals = self.rows + self.cols
        return any([not s for s in vals])

    def get_score(self):
        return self.unmarked_sum * self.last_num_called

def read_boards(lines):
    nums = [int(i) for i in lines[0].strip().split(',')]
    boards = []
    curBoard = []
    for row in lines[2:] + ['']:
        if not row:
            if len(curBoard) != 0:
                boards.append(BingoBoard(curBoard))
                curBoard = []
        else:
            curBoard.append(row)
    return nums, boards

def parse(fn):
    with open(fn) as f:
        return [l.strip() for l in f]

def part1(data):
    (nums, boards) = read_boards(data)
    for n in nums:
        for i, b in enumerate(boards):
            b.call_number(n)
            if b.has_won():
                return b.get_score()

def part2(data):
    (nums, boards) = read_boards(data)
    for n in nums:
        for b in boards:
            b.call_number(n)
        if len(boards) == 1 and boards[0].has_won():
            return boards[0].get_score()
        boards = filter(lambda x: not x.has_won(), boards)

if __name__ == "__main__":
    data = parse(sys.argv[1])
    print(part1(data))
    print(part2(data))