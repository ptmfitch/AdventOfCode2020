import re

input_regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'


def valid_password(mn, mx, char, password):
    if len(password) >= mx:
        a = password[mn - 1] == char
        b = password[mx - 1] == char
        return a ^ b
    elif len(password) > mn:
        return password[mn - 1] == char
    else:
        return False


count = 0
with open('inputs/day2.txt') as input_file:
    for line in input_file:
        match = re.match(input_regex, line)
        if valid_password(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)):
            count += 1
print(count)
