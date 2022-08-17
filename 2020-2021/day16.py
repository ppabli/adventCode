import re
from functools import reduce

raw_data = open('./data/day16.data.txt', 'r').read()

rules_raw, myticket, near_raw = [section.split('\n') for section in raw_data.split('\n\n')]

rules = {}
for rule in rules_raw:
	search = rule.split(":")
	name = search[0]
	nums = [int(n) for part in search[1].split("or") for n in part.split("-") ]
	rules[name] = nums

myticket = [int(x) for x in myticket[1].split(",")]
near = [[int(x) for x in line.split(",")] for line in near_raw[1:]]

def is_valid(i, rules):
	return any([rule_value[0] <= i <= rule_value[1] or rule_value[2] <= i <= rule_value[3] for rule_value in rules.values()])

def part1():

	total = sum(value for ticket in near for value in ticket if not is_valid(value, rules))
	print(total)

part1()

def product(array):
	return reduce((lambda x, y: x * y), array)

def part2():

	valid = [ticket for ticket in near if all([is_valid(value, rules) for value in ticket])]

	possibles = {}
	for name, values in rules.items():
		possibles[name] = [i for i in range(len(rules)) if all([is_valid(t[i], {name: values}) for t in valid])]

	matched = {}
	for name, possibilities in sorted(possibles.items(), key=lambda x: len(x[1])):
		index = [i for i in possibilities if i not in matched]
		assert len(index) == 1
		matched[index[0]] = name

	res = product([x for i, x in enumerate(myticket) if "departure" in matched[i]])

	print(res)

part2()
