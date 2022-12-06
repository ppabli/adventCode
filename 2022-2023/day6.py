data = open('./data/day6.data.txt', 'r').read().strip()

def part1():

	length = 4

	for index in range(len(data)):

		if (len(set(data[index: index + length])) == length):

			print(index + length)
			break

part1()

def part2():

	length = 14

	for index in range(len(data)):

		if (len(set(data[index: index + length])) == length):

			print(index + length)
			break

part2()