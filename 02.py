from operator import xor

def load(path):
    with open(path, 'r') as raw:
        passwords = [line.strip() for line in raw.readlines()]
        processed = []
        for line in passwords:
            line = line.split(': ', 1)
            password = line[1]
            line[0] = line[0].split(' ')
            target_char = line[0][1]
            min_char, max_char = [int(i) for i in line[0][0].split('-')]
            processed.append([min_char, max_char, target_char, password])
        return processed

def part1(path):
    passwords = load(path)
    good_pw = 0
    for x in passwords:
        min_c, max_c, target, password = x
        if min_c <= password.count(target) <= max_c:
            good_pw += 1
    return good_pw

def part2(path):
    passwords = load(path)
    good_pw = 0
    for x in passwords:
        pos1, pos2, target, password = x
        pos1, pos2 = pos1 - 1, pos2 - 1 # Supplied data not zero indexed
        if xor(password[pos1] == target,  password[pos2] == target):
            good_pw += 1
    return good_pw
