from collections import defaultdict

raw_data = open('./data/day15.data.txt', 'r').read().split("\n")

inputs = [int(x) for x in raw_data[0].split(",")]

def part1():

	nums = defaultdict(list)

	for i, n in enumerate(inputs):
		nums[n].append(i)

	last = n

	for i in range(len(inputs), 30000000):

		if len(nums[last]) < 2:

			nums[0].append(i)
			last = 0

		else:

			last = nums[last][-1] - nums[last][-2]
			nums[last].append(i)

		if i == 2019:
			break

	print(last)

part1()

def part2():

	nums = defaultdict(list)

	for i, n in enumerate(inputs):
		nums[n].append(i)

	last = n

	for i in range(len(inputs), 30000000):

		if len(nums[last]) < 2:

			nums[0].append(i)
			last = 0

		else:

			last = nums[last][-1] - nums[last][-2]
			nums[last].append(i)

	print(last)

part2()