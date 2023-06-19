from string import ascii_lowercase as asc
from heapq import heappop, heappush

data = open('./data/day12.data.txt', 'r').read().split('\n')

def neighborsPart1(i, j, grid, n, m):

	for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

		ii = i + di
		jj = j + dj

		if not (0 <= ii < n and 0 <= jj < m):

			continue

		if grid[ii][jj] <= grid[i][j] + 1:

			yield ii, jj

def neighborsPart2(i, j, grid, n, m):

	for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

		ii = i + di
		jj = j + dj

		if not (0 <= ii < n and 0 <= jj < m):

			continue

		if grid[ii][jj] >= grid[i][j] - 1:

			yield ii, jj

def part1():

	grid = []
	start, end = [-1, -1]

	n = len(data)
	m = len(data[0])

	for row, line in enumerate(data):

		newLine = []

		for col, char in enumerate(line):

			if char in asc:

				newLine.append(asc.index(char))

			elif char == 'E':

				newLine.append(25)
				end = (row, col)

			elif char == 'S':

				newLine.append(0)
				start = (row, col)

		grid.append(newLine)

	visited = [[False] * m for _ in range(n)]
	heap = [(0, start[0], start[1])]

	while True:

		steps, i, j = heappop(heap)

		if visited[i][j]:

			continue

		visited[i][j] = True

		if (i, j) == end:

			print(steps)
			break

		for ii, jj in neighborsPart1(i, j, grid, n, m):

			heappush(heap, (steps + 1, ii, jj))

part1()

def part2():

	grid = []
	start, end = [-1, -1]

	n = len(data)
	m = len(data[0])

	for row, line in enumerate(data):

		newLine = []

		for col, char in enumerate(line):

			if char in asc:

				newLine.append(asc.index(char))

			elif char == 'E':

				newLine.append(25)
				end = (row, col)

			elif char == 'S':

				newLine.append(0)
				start = (row, col)

		grid.append(newLine)

	visited = [[False] * m for _ in range(n)]
	heap = [(0, end[0], end[1])]

	while True:

		steps, i, j = heappop(heap)

		if visited[i][j]:

			continue

		visited[i][j] = True

		if grid[i][j] == 0:

			print(steps)
			break

		for ii, jj in neighborsPart2(i, j, grid, n, m):

			heappush(heap, (steps + 1, ii, jj))

part2()