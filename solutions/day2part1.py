import re

input_regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'


def valid_password(mn, mx, char, password):
    n = 0
    for c in password:
        if c == char:
            n += 1
    return mn <= n <= mx


count = 0
with open('../inputs/day2.txt') as input_file:
    for line in input_file:
        match = re.match(input_regex, line)
        if valid_password(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)):
            count += 1
print(count)
