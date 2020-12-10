from itertools import combinations

def load(path):
    with open(path, 'r') as raw:
        return [int(x) for x in raw.read().strip().split('\n')]

def part1(data, verbose = False):
    a = sorted(list(data) + [0] + [max(data) + 3])
    diffs = []
    for i in range(1, len(a)):
        diffs.append(a[i] - a[i-1])
    if verbose: 
        print(diffs.count(1) * diffs.count(3))
    return diffs

def check_perm(p):
    if set(part1(p)).difference(set([1,2,3])):
        return False
    else:
        return True

def calc_perms(n):
    x = [1] + list(range(4, 4+n+1))
    x += [max(x) + 3]
    x = tuple(x)
    ncr = []
    for i in range(1,len(x)+1):
        ncr += list(combinations(x,i))
    ncr = [a for a in ncr if a[0] == 1 and a[-1] == max(x)]
    valid_ncr = []
    for comb in ncr:
        if check_perm(comb):
            valid_ncr.append(comb)
    return len(valid_ncr)

def part2(data):
    diffs = part1(data)
    # Create a list of "runs" of +1 jolts
    string = ''.join([str(x) for x in diffs])
    groups = [x for x in string.split('3') if x != '']
    print(groups)
    # Each "run" produces branches
    branches = [calc_perms(len(x)) for x in groups]
    # Branches multiplied out to get solution
    product = 1
    for n in branches:
        product *= n
    return product

 
