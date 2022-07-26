import numpy as np

raw_data = open('./data/day11.data.txt', 'r').read().split('\n')

def checkFlash(data, checkedPos, x, y):

	if data[x][y] <= 9:

		return 0

	checkedPos[x][y] = 1
	data[x][y] = 0
	temp = 0

	# Top
	if x - 1 >= 0 and checkedPos[x - 1][y] == 0:

		data[x - 1][y] += 1
		temp += checkFlash(data, checkedPos, x - 1, y)

	# Bottom
	if x + 1 < len(data) and checkedPos[x + 1][y] == 0:

		data[x + 1][y] += 1
		temp += checkFlash(data, checkedPos, x + 1, y)

	# Left
	if y - 1 >= 0 and checkedPos[x][y - 1] == 0:

		data[x][y - 1] += 1
		temp += checkFlash(data, checkedPos, x, y - 1)

	# Right
	if y + 1 < len(data[x]) and checkedPos[x][y + 1] == 0:

		data[x][y + 1] += 1
		temp += checkFlash(data, checkedPos, x, y + 1)

	# Top - Right
	if y + 1 < len(data[x]) and x - 1 >= 0 and checkedPos[x - 1][y + 1] == 0:

		data[x - 1][y + 1] += 1
		temp += checkFlash(data, checkedPos, x - 1, y + 1)

	# Top - Left
	if y - 1 >= 0 and x - 1 >= 0 and checkedPos[x - 1][y - 1] == 0:

		data[x - 1][y - 1] += 1
		temp += checkFlash(data, checkedPos, x - 1, y - 1)

	# Bottom - Right
	if y + 1 < len(data[x]) and x + 1 < len(data) and checkedPos[x + 1][y + 1] == 0:

		data[x + 1][y + 1] += 1
		temp += checkFlash(data, checkedPos, x + 1, y + 1)

	# Bottom - Left
	if y - 1 >= 0 and x + 1 < len(data) and checkedPos[x + 1][y - 1] == 0:

		data[x + 1][y - 1] += 1
		temp += checkFlash(data, checkedPos, x + 1, y - 1)

	return temp + 1

def part1():

	steps = 100
	total = 0

	data = np.array([[int(x) for x in list(i)] for i in raw_data])
	size = len(data)

	for step in range(steps):

		# First update by one
		for row in range(size):

			for col in range(size):

				data[row][col] += 1

		checkedPos = np.zeros((size, size))

		for row in range(size):

			for col in range(size):

				total += checkFlash(data, checkedPos, row, col)

	print(total)

part1()

def part2():

	steps = 0

	data = np.array([[int(x) for x in list(i)] for i in raw_data])
	size = len(data)

	while True:

		steps += 1

		# First update by one
		for row in range(size):

			for col in range(size):

				data[row][col] += 1

		checkedPos = np.zeros((size, size))

		total = 0

		for row in range(size):

			for col in range(size):

				total += checkFlash(data, checkedPos, row, col)

		if total == 100:

			break

	print(steps)

part2()