raw_data = open('day9.data.txt', 'r').read().split('\n')

def part1():

	points = []

	data = [[int(i) for i in list(line)] for line in raw_data]

	rows = len(data)
	cols = len(data[0])

	for row in range(rows):

		for col in range(cols):

			value = data[row][col]
			valid = True

			# Top value
			if row - 1 >= 0 and data[row - 1][col] <= value:

				valid = False

			# Right value
			if col + 1 < cols and data[row][col + 1] <= value:

				valid = False

			# Bottom value
			if row + 1 < rows and data[row + 1][col] <= value:

				valid = False

			# Left value
			if col - 1 >= 0 and data[row][col - 1] <= value:

				valid = False

			if valid:

				points.append(value + 1)

	print(points)
	print(sum(points))

part1()

import numpy as np

def checkPos(data, checkedPos, x, y):

	if data[x][y] == 9:

		return 0

	checkedPos[x][y] = 1
	temp = 0

	if x - 1 >= 0 and checkedPos[x - 1][y] == 0:

		temp += checkPos(data, checkedPos, x - 1, y)

	if x + 1 < len(data) and checkedPos[x + 1][y] == 0:

		temp += checkPos(data, checkedPos, x + 1, y)

	if y - 1 >= 0 and checkedPos[x][y - 1] == 0:

		temp += checkPos(data, checkedPos, x, y - 1)

	if y + 1 < len(data[x]) and checkedPos[x][y + 1] == 0:

		temp += checkPos(data, checkedPos, x, y + 1)

	return temp + 1

def part2():

	points = []

	data = [[int(i) for i in list(line)] for line in raw_data]

	rows = len(data)
	cols = len(data[0])

	for row in range(rows):

		for col in range(cols):

			value = data[row][col]
			valid = True

			# Top value
			if row - 1 >= 0 and data[row - 1][col] <= value:

				valid = False

			# Right value
			if col + 1 < cols and data[row][col + 1] <= value:

				valid = False

			# Bottom value
			if row + 1 < rows and data[row + 1][col] <= value:

				valid = False

			# Left value
			if col - 1 >= 0 and data[row][col - 1] <= value:

				valid = False

			if valid:

				points.append((row, col))

	basins = []
	checkedPos = np.zeros((rows, cols))

	for point in points:

		basins.append(checkPos(data, checkedPos, point[0], point[1]))

	sortedValues = sorted(basins, reverse=True)[:3]
	print(sortedValues)
	print(sortedValues[0] * sortedValues[1] * sortedValues[2])

part2()
