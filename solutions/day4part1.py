from utils import inputs

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate(passport):
    if len(passport.split(' ')) < 7:
        return 0
    for req in req_fields:
        if req+':' not in passport:
            return 0
    return 1


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
