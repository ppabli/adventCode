from functools import reduce

raw_data = open('./data/day13.data.txt', 'r').read().split('\n')

def part1():

	start = int(raw_data[0])

	buses = [int(b) for b in raw_data[1].split(",") if b != "x"]
	waits = [(b, b - (start % b)) for b in buses]

	answer = min(waits, key=lambda x: x[1])

	print(answer[0] * answer[1])

part1()

def part2():

	busses = raw_data[1].split(",")

	bi = []
	ni = []

	for i in range(len(busses)):

		if busses[i] != "x":

			bi.append((int(busses[i]) - i % int(busses[i])) % int(busses[i]))
			ni.append(int(busses[i]))

	N = 1

	for n in ni:
		N *= n

	Ni = [N // n for n in ni]
	xi = []
	product = []

	for i in range(len(Ni)):

		num = Ni[i] % ni[i]
		found = False
		x = 1

		while not found:

			if (x * num) % ni[i] == 1:
				found = True
				break

			x += 1

		xi.append(x)

	for i in range(len(bi)):
		product.append(bi[i] * Ni[i] * xi[i])

	print(sum(product) % N)

part2()