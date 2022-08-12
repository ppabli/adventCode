from itertools import combinations

raw_data = open('./data/day9.data.txt', 'r').read().split("\n")

numbers = [int(i) for i in raw_data]

def part1():

	for i in range(len(numbers)):

		if i < 25:

			continue

		prev_numbers = numbers[i - 25:i]
		num = numbers[i]

		combs = combinations(prev_numbers, 2)

		if all([x + y != num for x, y in combs]):

			print(num)
			break

part1()

def part2():

	n = -1

	for i in range(len(numbers)):

		if i < 25:

			continue

		prev_numbers = numbers[i - 25:i]
		num = numbers[i]

		combs = combinations(prev_numbers, 2)

		if all([x + y != num for x, y in combs]):

			n = num
			break

	done = False
	res = -1

	for i in range(len(numbers)):
		for j in range(i + 1, len(numbers)):
			s = numbers[i:j]
			if sum(s) == n:
				res = min(s) + max(s)
				# Could be multiple values, we pick just the first one
				done = True
				break
		if done:
			break

	print(res)

part2()
