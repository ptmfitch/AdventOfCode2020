with open('inputs/day8.txt') as input_file:
    input_lines = input_file.readlines()

i = 0
acc = 0
seen = []

while i not in seen:
    seen.append(i)

    split = input_lines[i].rstrip().split(' ')
    inst = split[0]
    data = split[1]

    if inst == 'nop':
        i += 1
    elif inst == 'acc':
        acc += int(data)
        i += 1
    elif inst == 'jmp':
        i += int(data)

print(acc)
