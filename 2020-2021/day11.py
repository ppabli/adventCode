raw_data = open('./data/day11.data.txt', 'r').read().split("\n")

def part1():

	chairs = raw_data

	R = len(chairs)
	C = len(chairs[0])
	neigh = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	next_chairs = [["x" for c in r] for r in chairs]

	while True:

		changed = False

		for r in range(R):

			for c in range(C):

				num_occ = sum([chairs[r + y][c + x] == "#" for x, y in neigh if 0 <= r + y < R and 0 <= c + x < C])

				if chairs[r][c] == "L" and num_occ == 0:

					next_chairs[r][c] = "#"
					changed = True

				elif chairs[r][c] == "#" and num_occ >= 4:

					next_chairs[r][c] = "L"
					changed = True

				else:

					next_chairs[r][c] = chairs[r][c]

		if not changed:

			break

		chairs = [[next_chairs[r][c] for c in range(C)] for r in range(R)]

	print(sum([sum([chairs[r][c] == "#" for c in range(C)]) for r in range(R)]))

part1()

def part2():

	chairs = raw_data

	R = len(chairs)
	C = len(chairs[0])
	neigh = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	next_chairs = [["x" for c in r] for r in chairs]

	while True:

		changed = False

		for r in range(R):

			for c in range(C):

				num_occ = 0

				for dr, dc in neigh:

					x = c + dc
					y = r + dr

					while 0 <= x < C and 0 <= y < R and chairs[y][x] == ".":

						x += dc
						y += dr

					if 0 <= x < C and 0 <= y < R and chairs[y][x] == "#":

						num_occ += 1

				if chairs[r][c] == "L" and num_occ == 0:

					next_chairs[r][c] = "#"
					changed = True

				elif chairs[r][c] == "#" and num_occ >= 5:

					next_chairs[r][c] = "L"
					changed = True

				else:

					next_chairs[r][c] = chairs[r][c]

		if not changed:

			break

		chairs = [[next_chairs[r][c] for c in range(C)] for r in range(R)]

	print(sum([sum([chairs[r][c] == "#" for c in range(C)]) for r in range(R)]))

part2()
