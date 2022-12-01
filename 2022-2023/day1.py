data = open('./data/day1.data.txt', 'r').read().strip()

def part1():

	values = []

	for group in (data.split('\n\n')):
		value = 0
		for x in group.split('\n'):
			value += int(x)
		values.append(value)

	print(max(values))

part1()

def part2():

	values = []

	for group in (data.split('\n\n')):
		value = 0
		for x in group.split('\n'):
			value += int(x)
		values.append(value)

	values.sort(reverse = True)

	print(sum(values[:3]))

part2()