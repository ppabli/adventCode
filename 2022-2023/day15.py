data = open('./data/day15.data.txt', 'r').read().strip().split("\n")

beacons = []
sensors = []

for line in data:

	parts = line.split(" ")

	sx = int(parts[2][2:-1])
	sy = int(parts[3][2:-1])
	bx = int(parts[8][2:-1])
	by = int(parts[9][2:])

	sensors.append((sx, sy))
	beacons.append((bx, by))

dists = []

for i in range(len(sensors)):

	dist = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])

	dists.append(dist)

y = 2000000

intervals = []

positives = []
negatives = []

for index, sensor in enumerate(sensors):

	negatives.extend([sensor[0] + sensor[1] - dists[index], sensor[0] + sensor[1] + dists[index]])
	positives.extend([sensor[0] - sensor[1] - dists[index], sensor[0] - sensor[1] + dists[index]])

	diffX = dists[index] - abs(sensor[1] - y)

	if diffX <= 0:

		continue

	intervals.append((sensor[0] - diffX, sensor[0] + diffX))

minX = min([i[0] for i in intervals])
maxX = max([i[1] for i in intervals])

def part1():

	total = 0

	notValidX = [b[0] for b in beacons if b[1] == y]

	for x in range(minX, maxX + 1):

		if x in notValidX:

			continue

		if x <= any([i[0] for i in intervals]) or x >= any([i[1] for i in intervals]):

			total += 1

	print(total)

#part1()

def part2():

	pos = None
	neg = None

	n = len(sensors)

	for i in range(2 * n):

		for j in range(i + 1, 2 * n):

			a, b = positives[i], positives[j]

			if abs(a - b) == 2:

				pos = min(a, b) + 1

			a, b = negatives[i], negatives[j]

			if abs(a - b) == 2:

				neg = min(a, b) + 1

	cx = (pos + neg) // 2
	cy = (neg - pos) // 2

	print(cx * 4000000 + cy)

part2()