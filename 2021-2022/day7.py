raw_data = open('./data/day7.data.txt', 'r').read().split(',')

def part1():

	data = [int(i) for i in raw_data]

	sol = 1 << 60

	max_pos = max(data)

	for future_pos in range(max_pos):

		total = 0

		for actual_pos in data:

			dist = abs(actual_pos - future_pos)
			total += dist

		sol = min(total, sol)

	print(sol)

part1()

def part2():

	data = [int(i) for i in raw_data]

	sol = 1 << 60

	max_pos = max(data)

	for future_pos in range(max_pos):

		total = 0

		for actual_pos in data:

			dist = abs(actual_pos - future_pos)
			cost = dist * (dist + 1) // 2 #sum of n (dist value) first positive numbers

			total += cost

		sol = min(total, sol)

	print(sol)

part2()