from utils import inputs

rows = 127
cols = 7

def calc_id(row, col):
    return row * 8 + col


def binary_search(s, mx, lw, up):
    mn = 0
    for i, c in enumerate(s):
        if i == len(s) - 1:
            if c == up:
                return mx
            else:
                return mn
        if c == up:
            mn = ((mn + mx) + 1) / 2
        else:
            mx = ((mn + mx) - 1) / 2

ls = inputs.file_to_list("inputs/day5.txt")

ids = []
for bp in ls:
    r = binary_search(bp[:7], rows, 'F', 'B')
    c = binary_search(bp[7:], cols, 'L', 'R')
    ids.append(calc_id(r, c))
print(max(ids))



