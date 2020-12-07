from utils import inputs

rows = 127
cols = 7


def calc_id(row, col):
    return row * 8 + col


def missing_seat(row):
    for seat in range(0, 7):
        if seat not in row:
            return seat


def binary_search(s, mx, up):
    mn = 0
    for n, char in enumerate(s):
        if n == len(s) - 1:
            if char == up:
                return mx
            else:
                return mn
        if char == up:
            mn = ((mn + mx) + 1) / 2
        else:
            mx = ((mn + mx) - 1) / 2


ls = inputs.file_to_list("inputs/day5.txt")


plane = {}
for i in range(0, rows):
    plane[i] = []
for bp in ls:
    r = binary_search(bp[:7], rows, 'B')
    c = binary_search(bp[7:], cols, 'R')
    plane[r].append(c)
for r in range(0, rows):
    if len(plane[r]) == 7:
        c = missing_seat(plane[r])
        print(calc_id(r, c))
