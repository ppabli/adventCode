from z3 import If, Int, Optimize

input_data = open('./data/day24.data.txt', 'r').read().split("\n")

def print_data():

	line_len = 18
	for line_start in range(0, len(input_data), line_len):

		print(input_data[line_start:line_start + line_len])

# Variable div values in each line
a = [1, 1, 1, 26, 1, 1, 1, 26, 1, 26, 26, 26, 26, 26]

# Variable add values in each line
b = [13, 12, 10, -11, 14, 13, 12, -5, 10, 0, -11, -13, -13, -11]
c = [8, 16, 4, 1, 13, 5, 0, 10, 7, 2, 13, 15, 14, 9]

def solve(part1):

	s = Optimize()

	w = [Int(f"w{i}") for i in range(14)]
	for wi in w:

		s.add(wi >= 1, wi <= 9)
		(s.maximize if part1 else s.minimize)(wi)

	z = 0
	for wi, ai, bi, ci in zip(w, a, b, c):
		z = If(z % 26 + bi == wi, z / ai, z / ai * 26 + wi + ci)

	s.add(z == 0)
	s.check()

	return sum(10 ** (13 - i) * s.model()[wi].as_long() for i, wi in enumerate(w))

def part1():
	#print_data()
	print(solve(True))

part1()

def part2():
	#print_data()
	print(solve(False))

part2()