raw_data = open('./data/day12.data.txt', 'r').read().split('\n')

data = [(line[0], int(line[1:])) for line in raw_data]

dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
rot = {'L': 1j, 'R': -1j}

def part1():

	loc = 0
	d = 1

	for a, value in data:
		if a in dirs:
			loc += dirs[a] * value
		elif a in rot:
			d *= rot[a] ** (value/90)
		else:
			loc += d * value

	print(int(abs(loc.real) + abs(loc.imag)))

part1()

def part2():

	loc = 0
	waypoint = 10 + 1j

	for a, value in data:
		if a in dirs:
			waypoint += dirs[a] * value
		elif a in rot:
			waypoint *= rot[a] ** (value/90)
		else:
			loc += waypoint * value

	print(int(abs(loc.real) + abs(loc.imag)))

part2()