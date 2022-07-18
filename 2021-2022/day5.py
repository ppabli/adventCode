import numpy as np

data = open('day5.data.txt', 'r').read().split('\n')

def calculateValidPos(valueMap):

	total = 0;

	for value in valueMap.flatten():

		total += value > 1

	return total

def initializeMap():

	return np.zeros((1000, 1000))

def getSign(value):

	if value > 0:

		return 1

	elif value < 0:

		return -1

	else:

		return 0

def part1():

	dataMap = initializeMap()

	for i in range(0, len(data)):

		part1, part2 = data[i].split(' -> ')

		x1, y1 = map(int, part1.split(','))
		x2, y2 = map(int, part2.split(','))

		xDir = getSign(x2 - x1)
		yDir = getSign(y2 - y1)

		# Diagonal not valid
		if xDir != 0 and yDir != 0:
			continue

		while x1 != x2 or y1 != y2:

			dataMap[x1][y1] += 1

			x1 += xDir
			y1 += yDir

		dataMap[x1][y1] += 1

	print(calculateValidPos(dataMap))

part1()

def part2():

	dataMap = initializeMap()

	for i in range(0, len(data)):

		part1, part2 = data[i].split(' -> ')

		x1, y1 = map(int, part1.split(','))
		x2, y2 = map(int, part2.split(','))

		xDir = getSign(x2 - x1)
		yDir = getSign(y2 - y1)

		while x1 != x2 or y1 != y2:

			dataMap[x1][y1] += 1

			x1 += xDir
			y1 += yDir

		dataMap[x1][y1] += 1

	print(calculateValidPos(dataMap))

part2()