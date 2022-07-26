raw_data = open('./data/day6.data.txt', 'r').read().split(',')

def part1():

	data = [int(i) for i in raw_data]
	days = 80

	for day in range(days):

		for i in range(len(data)):

			if data[i] == 0:

				data[i] = 6
				data.append(8)

			else:

				data[i] -= 1

	print(len(data))

part1()

def generateDict():

	d = {}
	m = 8

	for i in range(m + 1):
		d[i] = 0

	return d

def part2():

	data = [int(i) for i in raw_data]
	days = 256

	fish_by_days_left = generateDict()

	for fish in range(len(data)):

		fish_by_days_left[data[fish]] += 1

	for day in range(days):

		new_dict = generateDict()

		for key in fish_by_days_left:

			if key == 0:

				new_dict[6] += fish_by_days_left[key]
				new_dict[8] = fish_by_days_left[key]

			else:

				new_dict[key - 1] += fish_by_days_left[key]

		fish_by_days_left = new_dict

	total = 0
	for key in fish_by_days_left:
		total += fish_by_days_left[key]

	print(total)

part2()