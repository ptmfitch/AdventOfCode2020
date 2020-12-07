from utils import inputs

temp = []
c = 0
data = inputs.file_to_list('inputs/day6.txt')
last_index = len(data) - 1
for i, line in enumerate(data):
    if i == last_index:
        temp.append(line)
        c += len(set(''.join(temp)))
        print(c)
    elif line != '\n':
        temp.append(line.rstrip())
    else:
        c += len(set(''.join(temp)))
        temp = []
