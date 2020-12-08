def load(path):
    with open(path, 'r') as raw:
        x = raw.read().strip().split('\n')
    return x

def part1(code):
    acc = 0
    i = 0
    visited = []
    while i not in visited:
        visited.append(i)
        inst, value = code[i].split(' ')
        if inst == 'nop':
            i += 1
        elif inst == 'acc':
            acc += int(value)
            i += 1
        elif inst == 'jmp':
            i += int(value)
    return acc

def part2(code):
    length = len(code)
    f_code = tuple(code)
    for j in range(len(code)):
        acc = 0
        i = 0
        visited = []
        altered_code = list(f_code)
        if 'acc' in altered_code[j]:
            continue
        elif 'jmp' in altered_code[j]:
            altered_code[j] = altered_code[j].replace('jmp', 'nop')
        elif 'nop' in altered_code[j]:
            altered_code[j] = altered_code[j].replace('nop', 'jmp')
        while i not in visited:
            if i == length:
                return acc
            visited.append(i)
            inst, value = altered_code[i].split(' ')
            if inst == 'nop':
                i += 1
            elif inst == 'acc':
                acc += int(value)
                i += 1
            elif inst == 'jmp':
                i += int(value)



