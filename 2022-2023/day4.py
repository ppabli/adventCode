data = open('./data/day4.data.txt', 'r').read().strip()

def part1():

	total = 0

	lines = data.split('\n')

	for line in lines:

		h1, h2 = line.split(',')

		start1, end1 = map(int, h1.split('-'))
		start2, end2 = map(int, h2.split('-'))

		if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):

			total += 1

	print(total)

part1()

def part2():

	total = 0

	lines = data.split('\n')

	for line in lines:

		h1, h2 = line.split(',')

		start1, end1 = map(int, h1.split('-'))
		start2, end2 = map(int, h2.split('-'))

		s1 = set(range(start1, end1 + 1))
		s2 = set(range(start2, end2 + 1))

		finalSet = set.intersection(s1, s2)

		if (finalSet):

			total += 1

	print(total)

part2()