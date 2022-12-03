import numpy as np

data = open('./data/day3.data.txt', 'r').read().strip().split('\n')

def part1():

	values = []

	for line in data:

		sharedChararacters = []

		length = len(line)
		half = length // 2

		half1 = line[:half]
		half2 = line[half:]

		for char1 in half1:

			for char2 in half2:

				if char1 == char2:

					sharedChararacters.append(char1)

		unique = set(sharedChararacters)

		for char in unique:

			value = ord(char)

			if (char.islower()):

				values.append(value - 96)

			else:

				values.append(value - 38)

	print(sum(values))

part1()

def part2():

	values = []

	groups = np.array_split(data, len(data) / 3)

	for group in groups:

		shortestString = min(group, key = len)

		sharedChararacters = []

		for char in shortestString:

			if char in group[0] and char in group[1] and char in group[2]:

				sharedChararacters.append(char)

		unique = set(sharedChararacters)

		for char in unique:

			value = ord(char)

			if (char.islower()):

				values.append(value - 96)

			else:

				values.append(value - 38)

	print(sum(values))

part2()