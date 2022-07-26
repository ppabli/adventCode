import heapq
from collections import defaultdict

raw_data = open('./data/day15.data.txt', 'r').read().split('\n')

def part1():

	data = [[int(i) for i in line] for line in raw_data]

	rows = len(data)
	cols = len(data[0])

	cost = defaultdict(int)

	print(rows, cols)

	pq = [(0, 0, 0)]
	heapq.heapify(pq)
	visited = set()

	while len(pq) > 0:

		c, row, col = heapq.heappop(pq)

		if (row, col) in visited:
			continue
		visited.add((row, col))

		cost[(row, col)] = c

		if row == rows - 1 and col == cols - 1:
			break

		for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			rr = row + dr
			cc = col + dc
			if not (0 <= rr < rows and 0 <= cc < cols):
				continue

			heapq.heappush(pq, (c + data[rr][cc], rr, cc))

	print(cost[(rows - 1, cols - 1)])

part1()

def get(data, r, c, rows, cols):
	x = (data[r % rows][c % cols] + (r // rows) + (c // cols))
	return (x - 1) % 9 + 1

def part2():

	data = [[int(i) for i in line] for line in raw_data]

	rows = len(data) * 5
	cols = len(data[0]) * 5

	cost = defaultdict(int)

	print(rows, cols)

	pq = [(0, 0, 0)]
	heapq.heapify(pq)
	visited = set()

	while len(pq) > 0:

		c, row, col = heapq.heappop(pq)

		if (row, col) in visited:
			continue
		visited.add((row, col))

		cost[(row, col)] = c

		if row == rows - 1 and col == cols - 1:
			break

		for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			rr = row + dr
			cc = col + dc
			if not (0 <= rr < rows and 0 <= cc < cols):
				continue

			heapq.heappush(pq, (c + get(data, rr, cc, rows // 5, cols // 5), rr, cc))

	print(cost[(rows - 1, cols - 1)])

part2()