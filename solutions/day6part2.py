from utils import inputs

temp = []
c = 0
data = inputs.file_to_list('inputs/day6.txt')
last_index = len(data) - 1
for i, line in enumerate(data):
    if i == last_index:
        common_chars = set(temp[0])
        for s in temp:
            common_chars = common_chars.intersection(s)
        c += len(common_chars)
        print(c)
    elif line != '\n':
        temp.append(line.rstrip())
    else:
        common_chars = set(temp[0])
        for s in temp:
            common_chars = common_chars.intersection(s)
        c += len(common_chars)
        temp = []
