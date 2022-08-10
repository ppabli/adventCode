raw_data = open('./data/day2.data.txt', 'r').read().split('\n')

data = [x.split() for x in raw_data]

def part1():

	valid = 0

	for line in data:

		lo, hi = list(map(int, line[0].split('-')))
		char = line[1][0] # To remove the ':'
		valid += lo <= line[2].count(char) <= hi

	print(valid)

part1()

def part2():

	valid = 0

	for line in data:

		a, b = list(map(int, line[0].split('-')))
		char = line[1][0] # To remove the ':'
		valid += (line[2][a - 1] == char) ^ (line[2][b - 1] == char)

	print(valid)

part2()