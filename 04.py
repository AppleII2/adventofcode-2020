import re

def load(path):
    dictionaries = []
    with open(path, 'r') as raw:
        entries = raw.read().strip().split('\n\n')
        lists = [entry.replace('\n',' ').split(' ') for entry in entries]
        for passport in lists:
            dictionary = {}
            for field in passport:
                key, value = field.split(':')
                dictionary[key] = value
            dictionaries.append(dictionary)
    return dictionaries

def part1(passports):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for passport in passports:
        if all([field in passport.keys() for field in req_fields]):
            valid += 1
    return valid

def part2(passports):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = []
    for passport in passports:
        if all([field in passport.keys() for field in req_fields]):
            valid.append(passport)
    verified_count = 0
    allowed_hcl_char = re.compile(r'[^a-f0-9.]') # For hair color rules
    for i, passport in enumerate(valid):
        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue
        if 'cm' in passport['hgt']:
            if not 150 <= int(passport['hgt'].strip('cm')) <= 193:
                continue
        elif 'in' in passport['hgt']:
            if not 59 <= int(passport['hgt'].strip('in')) <= 76:
                continue
        else:
            continue
        if passport['hcl'][0] == "#" and len(passport['hcl']) == 7:
            if allowed_hcl_char.search(passport['hcl'][1:]):
                continue
        else:
            continue
        if not passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            continue
        if len(passport['pid']) == 9:
            try:
                x = int(passport['pid'])
            except ValueError:
                continue
        else:
            continue
        verified_count += 1
    return verified_count

