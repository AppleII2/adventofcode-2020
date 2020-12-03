slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def load(path):
    with open(path, 'r') as raw:
        return [line.strip() for line in raw.readlines()]

def part1(skimap):
    width = len(skimap[0])
    hits = 0
    for i, line in enumerate(skimap):
        position = i * 3 % width
        if line[position] == '#':
            hits += 1
    return hits


def part2(skimap, slope):
    # Slope format (steps x, steps y)
    width = len(skimap[0])
    hits = 0
    for i in range(0, len(skimap), slope[1]):
        line = skimap[i]
        position = i//slope[1] * slope[0] % width
        if line[position] == '#':
            hits += 1
    return hits

def run(f):
    skimap = load(f)
    product = 1
    print("Part 1 ", part1(skimap))
    for slope in slopes:
        product *= part2(skimap, slope)
    print("Part 2 ", product)
    return product
