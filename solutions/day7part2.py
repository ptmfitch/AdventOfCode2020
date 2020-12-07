import re

rule_dict = {}
with open("../inputs/day7.txt") as input_file:
    for line in input_file:
        rule_match = re.match(r'^([a-z]+ [a-z]+) bags contain (.*?)\.$', line.rstrip())
        parent_bag = rule_match.group(1)
        child_dict = {}
        for child in rule_match.group(2).split(', '):
            if child == 'no other bags':
                break
            child_match = re.match(r'^(\d+) ([a-z]+ [a-z]+) bags?$', child)
            child_dict[child_match.group(2)] = int(child_match.group(1))
        rule_dict[parent_bag] = child_dict

res = set()
root = 'shiny gold'


def loop(my_dict, root_key):
    stems = my_dict[root_key]
    total = 0
    for key, val in stems.items():
        total += val
        total += (loop(my_dict, key) * val)
    return total


print(loop(rule_dict, root))
