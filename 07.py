import pickle

# Part 1 and the load function are missing because I accidentally overwrote
# the file.

def load(path):
    with open('dict-pickle', 'rb') as file:
        x = pickle.load(file)
    return x

def part2(master_dict):
    def recurse(contents):
        if list(contents.values()) == ['no']:
            return 0
        else:
            return sum([int(v) + int(v) * int(recurse(master_dict[k])) for k, v in contents.items()])
    return recurse(master_dict['shiny gold'])
