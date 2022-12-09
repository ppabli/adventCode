data = open('./data/day9.data.txt', 'r').read().strip().split('\n')

MR = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
MC = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

def moveTail(h, t):

	diffRow = abs(h[0] - t[0])
	diffCol = abs(h[1] - t[1])

	if (diffCol <= 1 and diffRow <= 1):
		pass

	elif diffRow > 1 and diffCol > 1:

		t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)

	elif diffRow > 1:

		t = (h[0]-1 if t[0] < h[0] else h[0] + 1, h[1])

	elif diffCol > 1:

		t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)

	return t

def part1():

	h = (0, 0)
	t = (0, 0)

	visited = set()

	for line in data:

		mov, steps = line.split(' ')
		steps = int(steps)

		for _ in range(steps):

			h = (h[0] + MR[mov], h[1] + MC[mov])
			t = moveTail(h, t)

			visited.add(t)

	print(len(visited))

part1()

def part2():

	h = (0, 0)

	# Now we have 9 "tails" and one head
	tails = [(0, 0) for _ in range(9)]

	visited = set()

	for line in data:

		mov, steps = line.split(' ')
		steps = int(steps)

		for _ in range(steps):

			h = (h[0] + MR[mov], h[1] + MC[mov])
			tails[0] = moveTail(h, tails[0])

			for i in range(1, 9):

				tails[i] = moveTail(tails[i - 1], tails[i])

			visited.add(tails[8])

	print(len(visited))

part2()


