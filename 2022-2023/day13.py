from functools import cmp_to_key

data = open('./data/day13.data.txt', 'r').read().split('\n\n')

def compare(a, b):

	if isinstance(a, list) and isinstance(b, int):

		b = [b]

	if isinstance(b, list) and isinstance(a, int):

		a = [a]

	if isinstance(a, int) and isinstance(b, int):

		if a < b:

			return 1

		if a == b:

			return 0

		return -1

	if isinstance(a, list) and isinstance(b, list):

		index = 0

		while index < len(a) and index < len(b):

			res = compare(a[index], b[index])

			if res != 0:

				return res

			index += 1

		if index == len(a):

			if len(a) == len(b):

				return 0

			return 1

		return -1

def part1():

	total = 0

	for i, pair in enumerate(data):

		a, b = map(eval, pair.split("\n"))

		if compare(a, b) == 1:

			total += i + 1

	print(total)

part1()

data = open('./data/day13.data.txt', 'r').read().replace("\n\n", "\n").split("\n")

def part2():

	lists = list(map(eval, data))
	lists.append([[2]])
	lists.append([[6]])

	lists = sorted(lists, key = cmp_to_key(compare), reverse = True)

	for i, li in enumerate(lists):

		if li == [[2]]:
			a = i + 1

		if li == [[6]]:
			b = i + 1

	print(a * b)

part2()
