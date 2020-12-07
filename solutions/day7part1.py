import re

rule_dict = {}
with open("../inputs/day7.txt") as input_file:
    for line in input_file:
        rule_match = re.match(r'^([a-z]+ [a-z]+) bags contain (.*?)\.$', line.rstrip())
        parent_bag = rule_match.group(1)
        child_bags = []
        for child in rule_match.group(2).split(', '):
            if child == 'no other bags':
                break
            child_bags.append(re.match(r'^\d+ ([a-z]+ [a-z]+) bags?$', child).group(1))
        rule_dict[parent_bag] = child_bags

res = set()
root = 'shiny gold'


def loop(my_dict, root_key):
    ls = []
    for key, val in my_dict.items():
        if root_key in val:
            res.add(key)
            ls.append(key)
    for new_root in ls:
        loop(my_dict, new_root)


loop(rule_dict, root)
print(len(res))
