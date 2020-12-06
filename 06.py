from collections import Counter

def threelines(path):
    with open(path, 'r') as raw:
        x = [g.split('\n') for g in raw.read().strip().split('\n\n')]
    print(sum(Counter(sum([list(set().union(*g)) for g in x],[])).values()))
    print(sum(Counter(sum([list(set.intersection(*[set(r) for r in g])) for g in x],[])).values()))

def load(path):
    with open(path, 'r') as raw:
        responses = raw.read().strip().split('\n\n')
        responses = [group.split('\n') for group in responses]
    return responses

def part1(path):
    responses = load(path)
    sets = [set().union(*group) for group in responses]
    counts = Counter(sum([list(x) for x in sets],[]))
    return sum(counts.values())

def part2(path):
    responses = load(path)
    sets = [set.intersection(*[set(x) for x in group]) for group in responses]
    counts = Counter(sum([list(x) for x in sets],[]))
    return sum(counts.values())
