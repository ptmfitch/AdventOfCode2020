example_answer = 127
part1_answer = 10884537
invalid_number = part1_answer

with open("inputs/day9.txt") as input_file:
    up_to_invalid = []
    for line in input_file:
        x = int(line)
        if x == invalid_number:
            break
        up_to_invalid.append(x)

up_to_invalid.reverse()


def loop(cur, idx, buffer, start):
    a = up_to_invalid[idx]
    cur -= a
    buffer.append(a)
    if cur == 0:
        print(max(buffer) + min(buffer))
    elif cur < 0:
        loop(invalid_number, start + 1, [], start + 1)
    else:
        loop(cur, idx + 1, buffer, start)


loop(invalid_number, 0, [], 0)




