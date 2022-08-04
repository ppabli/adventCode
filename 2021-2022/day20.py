import numpy as np
from scipy.signal import convolve2d

input_data = open('./data/day20.data.txt', 'r').read().split("\n")

def part1():

	enhancement = np.array(list(input_data[0])) == "#"
	grid = np.array(list(map(list, input_data[2:]))) == "#"

	kernel = 2 ** np.arange(9).reshape(3, 3)

	for i in range(50):
		grid = enhancement[convolve2d(grid, kernel, fillvalue = i % 2)]
		if i == 1:
			break

	print(grid.sum())

part1()

def part2():

	enhancement = np.array(list(input_data[0])) == "#"
	grid = np.array(list(map(list, input_data[2:]))) == "#"

	kernel = 2 ** np.arange(9).reshape(3, 3)

	for i in range(50):
		grid = enhancement[convolve2d(grid, kernel, fillvalue = i % 2)]
		if i == 49:
			break

	print(grid.sum())

part2()