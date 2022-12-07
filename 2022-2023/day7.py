from collections import defaultdict
import math

data = open('./data/day7.data.txt', 'r').read().strip().split('\n')

def part1():

	path = []
	sizes = defaultdict(int)

	for line in data:

		keys = line.split()

		if (keys[1] == 'cd'):

			if (keys[2] == '..'):
				path.pop()
			else:
				path.append(keys[2])

		elif (keys[1] == 'ls' or keys[0] == 'dir'):

			continue

		else:

			sz = int(keys[0])
			for i in range(1, len(path) + 1):
				sizes['/'.join(path[:i])] += sz

	total = 0
	for k, v in sizes.items():
		if v <= 100000:
			total += v

	print(total)

part1()

def part2():

	path = []
	sizes = defaultdict(int)

	for line in data:

		keys = line.split()

		if (keys[1] == 'cd'):

			if (keys[2] == '..'):
				path.pop()
			else:
				path.append(keys[2])

		elif (keys[1] == 'ls' or keys[0] == 'dir'):

			continue

		else:

			sz = int(keys[0])
			for i in range(1, len(path) + 1):
				sizes['/'.join(path[:i])] += sz

	totalSize = 70000000
	updateSize = 30000000

	usedSize = sizes['/']

	freeSize = usedSize - (totalSize - updateSize)

	actualFreeSize = math.inf

	for k, v in sizes.items():
		if v >= freeSize:
			actualFreeSize = min(actualFreeSize, v)

	print(actualFreeSize)

part2()