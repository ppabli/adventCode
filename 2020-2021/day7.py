from collections import defaultdict

raw_data = open('./data/day7.data.txt', 'r').read()

rules = raw_data.split("\n")

bags = defaultdict(dict)

for rule in rules:
	parts = rule.split(" ")
	color = " ".join(parts[:2])
	in_parts = " ".join(parts[4:]).split(",")
	for part in in_parts:
		if not "no other bags" in part:
			sp = part.strip().split(" ")
			bags[color][" ".join(sp[1:3])] = int(sp[0])
		else:
			bags[color] = {}

def can_hold(in_color, out_color):
	if in_color in str(bags[out_color]):
		return True
	return any([can_hold(in_color, b) for b in bags[out_color]])


def num_inside(color):
	return sum([bags[color][b] * (1 + num_inside(b)) for b in bags[color]])


def part1():

	print(sum([can_hold("shiny gold", bag) for bag in bags]))

part1()

def part2():

	print(num_inside("shiny gold"))

part2()