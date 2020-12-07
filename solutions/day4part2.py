from utils import inputs
import re

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def year_in_range(start, end, year):
    return start <= int(year[4:]) <= end


def height_in_range(hgt):
    if hgt[len(hgt)-2:] == 'cm':
        try:
            return 150 <= int(hgt[4:7]) <= 193
        except ValueError:
            return False
    return 59 <= int(hgt[4:6]) <= 76


def detailed_check(passport):
    details = passport.split(' ')
    for d in details:
        prefix = d[:3]
        if prefix == 'byr':
            if not year_in_range(1920, 2002, d):
                return 0
        elif prefix == 'iyr':
            if not year_in_range(2010, 2020, d):
                return 0
        elif prefix == 'eyr':
            if not year_in_range(2020, 2030, d):
                return 0
        elif prefix == 'hgt':
            if not height_in_range(d):
                return 0
        elif prefix == 'hcl':
            if not re.fullmatch('^hcl:#[0-9a-f]{6}$', d):
                return 0
        elif prefix == 'ecl':
            if not re.fullmatch('^ecl:(?:amb|blu|brn|gry|grn|hzl|oth)$', d):
                return 0
        elif prefix == 'pid':
            if not re.fullmatch('^pid:[0-9]{9}$', d):
                return 0
    return 1


def validate(passport):
    if len(passport.split(' ')) < 7:
        return 0
    for req in req_fields:
        if req+':' not in passport:
            return 0
    return detailed_check(passport)


temp = []
c = 0
data = inputs.file_to_list('inputs/day4.txt')
last_index = len(data) - 1
for i, line in enumerate(data):
    if i == last_index:
        temp.append(line)
        c += validate(' '.join(temp))
        print(c)
    elif line != '\n':
        temp.append(line.rstrip())
    else:
        c += validate(' '.join(temp))
        temp = []
