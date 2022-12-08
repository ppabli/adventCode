import numpy as np

data = open('./data/day8.data.txt', 'r').read().strip().split('\n')

matrix = [list(map(int, list(line))) for line in data]

COLS = len(matrix)
ROWS = len(matrix[0])

matrix = np.array(matrix)

def part1():

	total = 0

	for row in range(ROWS):

		for col in range(COLS):

			treeHeight = matrix[row][col]

			if row == 0 or np.amax(matrix[:row, col]) < treeHeight:

				total += 1

			elif row == ROWS - 1 or np.amax(matrix[(row + 1):, col]) < treeHeight:

				total += 1

			elif col == 0 or np.amax(matrix[row, :col]) < treeHeight:

				total += 1

			elif col == COLS - 1 or np.amax(matrix[row, (col + 1):]) < treeHeight:

				total += 1

	print(total)

part1()

def part2():

	neigh = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	total = 0

	for row in range(ROWS):

		for col in range(COLS):

			treeHeight = matrix[row][col]
			score = 1

			for rr, cc in neigh:

				newRow = row + rr
				newCol = col + cc

				dist = 0

				while 0 <= newRow < ROWS and  0 <= newCol < COLS and matrix[newRow][newCol] < treeHeight:

					dist += 1

					newRow += rr
					newCol += cc

					if (0 <= newRow < ROWS and  0 <= newCol < COLS and matrix[newRow][newCol] >= treeHeight):
						dist += 1

				score *= dist

			total = max(total, score)

	print(total)

part2()