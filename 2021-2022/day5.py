data = open('day5.data.txt', 'r').read().split('\n')

def calculateValidPos(valueMap):

	total = 0;

	for x in range(0, 1000):

		for y in range(0, 1000):

			if (valueMap[x][y] > 1):

				total += 1

	return total

def initializeMap():

	ventMap = []

	for x in range(0, 1000):

		ventMap.append([])

		for y in range(0, 1000):

			ventMap[x].append(0)

	return ventMap

def part1():

	dataMap = initializeMap()

	for i in range(0, len(data)):

		part1, part2 = data[i].split(' -> ')

		x1, y1 = map(int, part1.split(','))
		x2, y2 = map(int, part2.split(','))

		if x1 == x2:

			if y1 < y2:

				while y1 <= y2:

					dataMap[x1][y1] += 1
					y1 += 1

			else:

				while y2 <= y1:

					dataMap[x1][y2] += 1
					y2 += 1

		elif y1 == y2:

			if x1 < x2:

				while x1 <= x2:

					dataMap[x1][y1] += 1
					x1 += 1

			else:

				while x2 <= x1:

					dataMap[x2][y1] += 1
					x2 += 1

	print(calculateValidPos(dataMap))

part1()

def part2():

	dataMap = initializeMap()

	for i in range(0, len(data)):

		part1, part2 = data[i].split(' -> ')

		x1, y1 = map(int, part1.split(','))
		x2, y2 = map(int, part2.split(','))

		if x1 == x2:

			if y1 < y2:

				while y1 <= y2:

					dataMap[x1][y1] += 1
					y1 += 1

			else:

				while y2 <= y1:

					dataMap[x1][y2] += 1
					y2 += 1

		elif y1 == y2:

			if x1 < x2:

				while x1 <= x2:

					dataMap[x1][y1] += 1
					x1 += 1

			else:

				while x2 <= x1:

					dataMap[x2][y1] += 1
					x2 += 1

		else:

			if y1 < y2 and x1 < x2:

				while y1 <= y2:

					dataMap[x1][y1] += 1
					y1 += 1
					x1 += 1

			elif y2 < y1 and x2 < x1:

				while y2 <= y1:

					dataMap[x1][y1] += 1
					y1 -= 1
					x1 -= 1

			elif y1 < y2 and x2 < x1:

				while y1 <= y2:

					dataMap[x1][y1] += 1
					y1 += 1
					x1 -= 1

			elif y2 < y1 and x1 < x2:

				while y2 <= y1:

					dataMap[x1][y1] += 1
					y1 -= 1
					x1 += 1

	print(calculateValidPos(dataMap))

part2()