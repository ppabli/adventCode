import numpy as np

data = open('./data/day10.data.txt', 'r').read().split('\n')

def part1():

	total = 0
	interesting = [20, 60, 100, 140, 180, 220]

	x = 1
	cycle = 0

	for line in data:

		values = line.split(' ')

		if values[0] == "noop":

			cycle += 1

			if cycle in interesting:
				total += cycle * x

		elif values[0] == "addx":

			cycle += 1

			if cycle in interesting:
				total += cycle * x

			cycle += 1

			if cycle in interesting:
				total += cycle * x

			x += int(values[1])

	print(total)

part1()

def part2():

	cycle = 0

	register = 0

	x = [
		['.'] * 40,
		['.'] * 40,
		['.'] * 40,
		['.'] * 40,
		['.'] * 40,
		['.'] * 40
	]

	x = np.array(x)

	for line in data:

		parts = line.split(" ")

		if parts[0] == "noop":

			row = cycle // 40
			col = cycle - (row * 40)

			if col == register + 1 or col == register or col == register + 2:

				x[row][col] = '##'

			else:

				x[row][col] = '..'

			cycle += 1

		elif parts[0] == "addx":

			value = int(parts[1])

			row = cycle // 40
			col = cycle - (row * 40)

			if col == register + 1 or col == register or col == register + 2:

				x[row][col] = '##'
				print('#', line, cycle, register, row, col)

			else:

				x[row][col] = '..'
				print('.', line, col, register, row, col)

			cycle += 1

			row = cycle // 40
			col = cycle - (row * 40)

			if col == register + 1 or col == register or col == register + 2:

				x[row][col] = '##'
				print('#', line, cycle, register, row, col)

			else:

				x[row][col] = '..'
				print('.', line, cycle, register, row, col)

			cycle += 1
			register += value

	for row in x:
		print("".join(row))

part2()