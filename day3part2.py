slope = []
with open("inputs/day3.txt") as input_file:
    for line in input_file:
        slope.append(line)
width = len(slope[0]) - 1
height = len(slope)


def traverse_slope(right, down):
    c = 0
    j = 0
    for i in range(0, height, down):
        if slope[i][j] == '#':
            c += 1
        j += right
        j %= width
    return c


print(
    traverse_slope(1, 1) *
    traverse_slope(3, 1) *
    traverse_slope(5, 1) *
    traverse_slope(7, 1) *
    traverse_slope(1, 2)
)
