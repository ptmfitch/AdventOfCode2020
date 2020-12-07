x = 0
c = 0
with open("../inputs/day3.txt") as input_file:
    for line in input_file:
        if line[x] == '#':
            c += 1
        x += 3
        x %= len(line) - 1
print(c)
