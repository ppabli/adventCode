raw_data = open('./data/day3.data.txt', 'r').read().split('\n')

def count(increment_x, increment_y):

	x = 0
	y = 0

	total = 0

	while y < len(raw_data):

		total += raw_data[y][x % len(raw_data[0])] == '#'

		x += increment_x
		y += increment_y

	return total

def part1():

	res = count(3, 1)
	print(res)

part1()

def part2():

	res = count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2)
	print(res)

part2()