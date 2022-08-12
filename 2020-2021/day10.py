from collections import Counter, defaultdict

raw_data = open('./data/day10.data.txt', 'r').read().split("\n")

adapters = [int(x) for x in raw_data]
adapters = sorted(adapters + [0, max(adapters) + 3])

def part1():

	diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
	hist = Counter(diffs)

	print(hist[1] * hist[3])

part1()

def part2():

	paths = defaultdict(int)
	paths[0] = 1
	for i in range(1, len(adapters)):
		for j in range(i)[::-1]:
			if adapters[i] - adapters[j] > 3:
				break
			paths[i] += paths[j]

	print(paths[len(adapters)-1])

part2()