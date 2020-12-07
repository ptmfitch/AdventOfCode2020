ints = []
with open("../inputs/day1.txt") as input_file:
    for line in input_file:
        ints.append(int(line))

for i in ints:
    for j in ints:
        x = 2020 - (i + j)
        if x > 0:
            for k in ints:
                if k == x:
                    print(i * j * k)
                    exit()
