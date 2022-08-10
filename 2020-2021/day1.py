import numpy as np
from itertools import combinations

raw_data = open('./data/day1.data.txt', 'r').read().split('\n')

data = [int(x) for x in raw_data]

def part1():

	for c in combinations(data, 2):
		if (sum(c)) == 2020:
			print(np.product(c))
			break

part1()

def part2():

	for c in combinations(data, 3):
		if (sum(c)) == 2020:
			print(np.product(c))
			break

part2()