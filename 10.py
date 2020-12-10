def load(path):
    with open(path, 'r') as raw:
        return [int(x) for x in raw.read().strip().split('\n')]

def part1(data):
    a = sorted(list(data) + [0] + [max(data) + 3])
    diffs = []
    for i in range(1, len(a)):
        diffs.append(a[i] - a[i-1])
    print(diffs.count(1) * diffs.count(3))
    return diffs

td = (16,10,15,5,1,11,7,19,6,12,4)
td1 = (1,4,5,6,7,8,11,14,15,16,17,20,23,24,25,28)

def part2(data):
    diffs = part1(data)
    # Create a list of "runs" of +1 jolts
    string = ''.join([str(x) for x in diffs])
    groups = [x for x in string.split('3') if x != '']
    print(groups)
    # Each "run" produces branches
    branches = [2 * (len(x) - 1) or 1 for x in groups]
    # Branches multiplied out to get solution
    product = 1
    for n in branches:
        product *= n
    return product

 
