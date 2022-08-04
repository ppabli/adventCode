import re
import numpy as np
from itertools import permutations, product, combinations
from collections import defaultdict

input_data = open('./data/day19.data.txt', 'r').read()

def get_scanners(raw_data):

	scanners = []

	for scanner_data in raw_data.split("\n\n"):

		data_lines = scanner_data.split("\n")[1:]
		data = np.array([list([int(i) for i in x.split(",")]) for x in data_lines])
		scanners.append(data)

	return scanners

def get_rotations():

	rotations = []

	for perm in permutations((0, 1, 2)):

		for signs in product((-1, 1), repeat = 3):

			if np.linalg.det(a := np.diag(signs)[:, perm]) > 0:

				rotations.append(a)

	return rotations

def overlaps(x, y, rotations, scanners):

	for rotation in rotations:

		count = defaultdict(int)

		for b1 in scanners[x]:

			for b2 in scanners[y]:

				position = tuple(b1 - b2 @ rotation)
				count[position] += 1

				if count[position] == 12:

					return position, position + scanners[y] @ rotation

def part1():

	scanners = get_scanners(input_data)
	rotations = get_rotations()

	stack = [0]
	done = set()
	positions = [(0, 0, 0)]

	while stack:

		i = stack.pop()
		done.add(i)

		for j in set(range(len(scanners))) - done:

			if overlap := overlaps(i, j, rotations, scanners):

				position, translated = overlap
				positions.append(position)
				scanners[j] = translated
				stack.append(j)

	print(len(set(tuple(s) for scanner in scanners for s in scanner)))

part1()

def part2():

	scanners = get_scanners(input_data)
	rotations = get_rotations()

	stack = [0]
	done = set()
	positions = [(0, 0, 0)]

	while stack:

		i = stack.pop()
		done.add(i)

		for j in set(range(len(scanners))) - done:

			if overlap := overlaps(i, j, rotations, scanners):

				position, translated = overlap
				positions.append(position)
				scanners[j] = translated
				stack.append(j)

	print(max(sum(abs(x1 - x2) for x1, x2 in zip(s1, s2)) for s1, s2 in combinations(positions, 2)))

part2()