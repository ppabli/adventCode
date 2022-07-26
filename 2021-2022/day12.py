import numpy as np

raw_data = open('./data/day12.data.txt', 'r').read().split('\n')

def checkCave1(cave, visited, caveSystem):

	if cave == 'end':

		return 1

	if cave.islower():

		if cave in visited:

			return 0

		else:

			visited.append(cave)

	temp = 0

	for newCave in caveSystem[cave]:

		if newCave == 'start':

			continue

		temp += checkCave1(newCave, visited, caveSystem)

	if cave.islower():

		visited.remove(cave)

	return temp

def part1():

	data = [i.split('-') for i in raw_data]

	caveSystem = {}
	visited = []

	for a, b in data:

		if a in caveSystem:

			caveSystem[a].append(b)

		else:

			caveSystem[a] = [b]

		if b in caveSystem:

			caveSystem[b].append(a)

		else:

			caveSystem[b] = [a]

	total = checkCave1('start', visited, caveSystem)

	print(total)

part1()


def checkCave2(cave, visited, caveSystem):

	if cave == 'end':

		return 1

	if cave.islower():

		visited[cave] += 1

		validCaves = 0
		for smallCave in visited:

			validCaves += visited[smallCave] > 1

			if visited[smallCave] > 2:
				visited[smallCave] -= 1

				return 0

		if validCaves > 1:

			visited[cave] -= 1
			return 0

	temp = 0

	for newCave in caveSystem[cave]:

		if newCave == 'start':

			continue

		temp += checkCave2(newCave, visited, caveSystem)

	if cave.islower():

		visited[cave] -= 1

	return temp

def part2():

	data = [i.split('-') for i in raw_data]

	caveSystem = {}
	visited = {}

	for a, b in data:

		if a not in visited:

			visited[a] = 0

		if b not in visited:

			visited[b] = 0

		if a in caveSystem:

			caveSystem[a].append(b)

		else:

			caveSystem[a] = [b]

		if b in caveSystem:

			caveSystem[b].append(a)

		else:

			caveSystem[b] = [a]

	total = checkCave2('start', visited, caveSystem)

	print(total)

part2()