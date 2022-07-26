import numpy as np

raw_data = open('./data/day13.data.txt', 'r').read().split('\n')

def foldY(dotMap, value):

	topArea = dotMap[:value]

	foldArea = dotMap[value + 1:]
	foldedArea = foldArea[::-1]

	for row in range(len(topArea)):

		for col in range(len(topArea[row])):

			if topArea[row][col] != 0 or foldedArea[row][col] != 0:

				topArea[row][col] = 1

	return topArea

def foldX(dotMap, value):

	rightArea = dotMap[:,:value]

	leftArea = dotMap[:,value + 1:]
	foldedArea = np.flip(leftArea, 1)

	for row in range(len(rightArea)):

		for col in range(len(rightArea[row])):

			if rightArea[row][col] != 0 or foldedArea[row][col] != 0:

				rightArea[row][col] = 1

	return rightArea

def part1():

	dots = raw_data[:len(raw_data) - 13]

	colDots = [int(i.split(',')[0]) for i in dots]
	rowDots = [int(i.split(',')[1]) for i in dots]

	instructions = raw_data[len(raw_data) - 12:]

	dotMap = np.zeros((max(rowDots) + 1, max(colDots) + 1), int)

	for x in range(len(colDots)):

		col = colDots[x]
		row = rowDots[x]

		dotMap[row][col] = 1

	ins = instructions[0]

	axis, value = ins.split('fold along ')[1].split('=')

	if axis == 'y':

		dotMap = foldY(dotMap, int(value))

	else:

		dotMap = foldX(dotMap, int(value))

	print(np.count_nonzero(dotMap))

part1()

def part2():

	dots = raw_data[:len(raw_data) - 13]

	colDots = [int(i.split(',')[0]) for i in dots]
	rowDots = [int(i.split(',')[1]) for i in dots]

	instructions = raw_data[len(raw_data) - 12:]

	dotMap = np.zeros((max(rowDots) + 1, max(colDots) + 1), int)

	for x in range(len(colDots)):

		col = colDots[x]
		row = rowDots[x]

		dotMap[row][col] = 1

	for ins in instructions:

		axis, value = ins.split('fold along ')[1].split('=')

		if axis == 'y':

			dotMap = foldY(dotMap, int(value))

		else:

			dotMap = foldX(dotMap, int(value))

	for row in range(len(dotMap)):

		for col in range(len(dotMap[row])):

			if dotMap[row][col] != 0:

				print('###', end='')

			else:

				print("...", end='')

part2()