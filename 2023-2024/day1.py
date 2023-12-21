import re

data = open('./data/day1.data.txt', 'r').read().strip()

def part1():

	data_list = data.split('\n')

	total = 0

	for line in data_list:

		res = re.findall(r'\d', line)

		if len(res) == 1:

			total += int(res[0] * 2)

		else:

			total += int(res[0] + res[-1])

	print(total)

#part1()

def part2():

	data_list = data.split('\n')

	nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

	total = 0

	for line in data_list:

		first = None
		second = None

		for index in range(len(line)):

			temp = None

			c = line[index]

			if c.isdigit():

				temp = int(c)

			for i, num in enumerate(nums):

				if line[index:index + len(num)] == num:

					temp = i + 1
					break

			if temp:

				if not first:

					first = temp

				second = temp

		total += first * 10 + second

	print(total)

part2()