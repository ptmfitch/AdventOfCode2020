ints = []
with open("inputs/day1.txt") as input_file:
    for line in input_file:
        i = int(line)
        for j in ints:
            if i == j:
                print((2020 - i) * j)
                exit()
        ints.append(2020 - i)
