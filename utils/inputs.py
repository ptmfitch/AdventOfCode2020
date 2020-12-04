def file_to_list(fp):
    ls = []
    with open(fp) as input_file:
        for line in input_file:
            ls.append(line)
    return ls


def file_length(fp):
    return sum(1 for line in fp)
