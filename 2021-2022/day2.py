data = open('day2.data.txt', 'r').read().split('\n')

def part1():

	x = 0
	y = 0

	for i in range(0, len(data) - 1):

		movement = data[i].split(' ')[0]
		value = data[i].split(' ')[1]

		if movement == "up":
			y -= int(value)
		elif movement == "down":
			y += int(value)
		elif movement == "forward":
			x += int(value)

	print(x, y, x * y)

part1()

def part2():

	x = 0
	y = 0
	aim = 0

	for i in range(0, len(data) - 1):

		movement = data[i].split(' ')[0]
		value = data[i].split(' ')[1]

		if movement == "up":
			aim -= int(value)
		elif movement == "down":
			aim += int(value)
		elif movement == "forward":
			x += int(value)
			y += aim * int(value)

	print(x, y, x * y)

part2()