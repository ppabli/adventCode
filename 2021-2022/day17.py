raw_data = open('./data/day17.data.txt', 'r').read()

splitted = raw_data.split(" ")

def part1():

	min_x, max_x = [int(i) for i in splitted[2][2:].replace(",", "").split("..")]
	min_y, max_y = [int(i) for i in splitted[3][2:].split("..")]

	vy = (abs(min_y) - 1)
	h_max = ((vy + 0.5) ** 2) / 2
	print(round(h_max))

part1()

def hit(x, y, min_x, min_y, max_x, max_y):

	initial_x = initial_y = 0

	while True:

		if initial_x > max_x:
			return False

		if x == 0 and not min_x <= initial_x <= max_x:
			return False

		if x == 0 and initial_y < min_y:
			return False

		if min_x <= initial_x <= max_x and min_y <= initial_y <= max_y:
			return True

		initial_x += x
		initial_y += y

		if x > 0:
			x -= 1

		y -= 1

def part2():

	min_x, max_x = [int(i) for i in splitted[2][2:].replace(",", "").split("..")]
	min_y, max_y = [int(i) for i in splitted[3][2:].split("..")]

	def hit(vx, vy):

		x = y = 0

		while True:
			# breaking conditions
			if x > max_x: return False
			if vx == 0 and not min_x <= x <= max_x: return False
			if vx == 0 and y < min_y: return False

			# target condition
			if min_x <= x <= max_x and min_y <= y <= max_y: return True

			x += vx
			y += vy

			if vx > 0: vx -= 1
			vy -= 1

	y_max = max(abs(min_y), abs(max_y))
	total = 0
	
	for vx in range(max_x + 1):
		for vy in range(-y_max, y_max + 1):
			total += hit(vx, vy)

	print(total)

part2()