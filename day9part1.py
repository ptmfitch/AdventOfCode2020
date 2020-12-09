def is_valid(check_me, ls):
    for sub_me in ls:
        if abs(check_me - sub_me) in ls:
            return True
    return False


with open("inputs/day9.txt") as input_file:
    n = 25
    i = 0
    buffer = []
    for line in input_file:
        x = int(line)
        if i < n:
            buffer.append(x)
        else:
            if not is_valid(x, buffer):
                print(x)
            buffer[i % n] = x
        i += 1
