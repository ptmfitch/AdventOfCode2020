with open('inputs/day8.txt') as input_file:
    input_lines = input_file.readlines()
    ln = len(input_lines)


def loop(ptr, acc, seen, branched):
    if ptr in seen:
        return
    seen.append(ptr)
    if ptr == ln:
        print(acc)
        exit()
    [inst, data] = input_lines[ptr].rstrip().split(' ')
    if inst == 'nop':
        if not branched:
            loop(ptr + int(data), acc, seen.copy(), True)
        loop(ptr + 1, acc, seen, branched)
    elif inst == 'acc':
        loop(ptr + 1, acc + int(data), seen, branched)
    elif inst == 'jmp':
        if not branched:
            loop(ptr + 1, acc, seen.copy(), True)
        loop(ptr + int(data), acc, seen, branched)


loop(0, 0, [], False)
