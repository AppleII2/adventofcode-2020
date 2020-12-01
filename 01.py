from itertools import combinations

def load(path):
    with open(path, 'r') as raw:
        return [int(line.strip()) for line in raw.readlines()]

def part1(path):
    expenses = load(path)
    for comb in list(combinations(expenses, 2)):
        if sum(comb) == 2020:
            return comb[0] * comb[1]

def part2(path):
    expenses = load(path)
    for comb in list(combinations(expenses, 3)):
        if sum(comb) == 2020:
            return comb[0] * comb[1] * comb[2]
