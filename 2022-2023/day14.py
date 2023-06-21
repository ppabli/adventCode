data = open('./data/day14.data.txt', 'r').read().split("\n")

filled = set()

def sandMovement1(maxY):

	sx, sy = 500, 0

	while sy <= maxY:

		if (sx, sy + 1) not in filled:

			sy += 1

			continue

		if (sx - 1, sy + 1) not in filled:

			sx -= 1
			sy += 1

			continue

		if (sx + 1, sy + 1) not in filled:

			sx += 1
			sy += 1

			continue

		filled.add((sx, sy))

		return True

	return False

def sandMovement2(maxY):

	sx, sy = 500, 0

	if (sx, sy) in filled:

		return (sx, sy)

	while sy <= maxY:

		if (sx, sy + 1) not in filled:

			sy += 1

			continue

		if (sx - 1, sy + 1) not in filled:

			sx -= 1
			sy += 1

			continue

		if (sx + 1, sy + 1) not in filled:

			sx += 1
			sy += 1

			continue

		break

	return (sx, sy)

def part1():

	for line in data:

		points = []

		for point in line.split(" -> "):

			x, y = map(int, point.split(","))

			points.append((x, y))

		for i in range(1, len(points)):

			cx, cy = points[i]
			px, py = points[i - 1]

			if cx != px:

				assert cy == py

				for x in range(min(cx, px), max(cx, px) + 1):

					filled.add((x, cy))

			if cy != py:

				assert cx == px

				for y in range(min(cy, py), max(cy, py) + 1):

					filled.add((cx, y))

	maxY = max([coord[1] for coord in filled])

	total = 0

	while True:

		res = sandMovement1(maxY)

		if not res:

			break

		total += 1

	print(total)

part1()

filled = set()

def part2():

	for line in data:

		points = []

		for point in line.split(" -> "):

			x, y = map(int, point.split(","))

			points.append((x, y))

		for i in range(1, len(points)):

			cx, cy = points[i]
			px, py = points[i - 1]

			if cx != px:

				assert cy == py

				for x in range(min(cx, px), max(cx, px) + 1):

					filled.add((x, cy))

			if cy != py:

				assert cx == px

				for y in range(min(cy, py), max(cy, py) + 1):

					filled.add((cx, y))

	maxY = max([coord[1] for coord in filled])

	total = 0

	while True:

		res = sandMovement2(maxY)

		filled.add(res)

		total += 1

		if res == (500, 0):

			break

	print(total)

part2()