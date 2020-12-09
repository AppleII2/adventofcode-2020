from itertools import combinations as ncr

def load(path):
    with open(path, 'r') as raw:
        return [int(i) for i in raw.read().strip().split('\n')]

def get_sum_ncr(table):
    return set([sum(i) for i in ncr(table, 2)])

def part1(data):
    preamble, encrypted = data[:25], data[25:]
    for i, line in enumerate(data[25:]):
        valid = get_sum_ncr(data[i:i+25])
        if line not in valid:
            print('index', i + 25)
            return line

def part2(data, index):
    target = data[index]
    data = data[:index] # Impossible to be above target, by manual inspection
    for i in range(0, len(data)-2):
        for j in range(2, len(data)):
            total = sum(data[i:j])
            if total == target:
                return min(data[i:j]) + max(data[i:j])
            elif total > target:
                break


