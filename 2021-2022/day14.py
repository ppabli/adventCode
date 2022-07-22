raw_data = open('day14.data.txt', 'r').read().split('\n')

def insert(list, var, i):
	new_list = list[:i]
	new_list.append(var)
	new_list.extend(list[i:])
	return new_list

def part1():

	initial = raw_data[0]
	steps = raw_data[2:]

	for i in range(10):

		if i == 0:
			initial = raw_data[0]

		else:
			initial = ''.join(map(str, final))

		final = [char for char in initial]

		totalAdded = 0

		for pairStart in range(len(initial) - 1):

			pairValue = initial[pairStart:pairStart + 2]

			for step in steps:

				key, value = step.split(' -> ')

				if key == pairValue:

					final = insert(final, value, pairStart + 1 + totalAdded)

					totalAdded += 1

	counts = [final.count(i) for i in final]

	res = max(counts) - min(counts)

	print(res)

#part1()

def part2():

	initial = raw_data[0]
	steps = raw_data[2:]

	pairs = {}
	for i in range(len(initial) - 1):
		key = initial[i:i + 2]
		if key in pairs:
			pairs[key] += 1
		else:
			pairs[key] = 1

	for i in range(40):

		temp = pairs.copy()

		for pair in pairs:

			for step in steps:

				key, value = step.split(' -> ')

				if pair == key:

					ocs = pairs[pair]
					temp[pair] -= ocs

					if pair[0] + value in temp:
						temp[pair[0] + value] += ocs
					else:
						temp[pair[0] + value] = ocs

					if value + pair[1] in temp:
						temp[value + pair[1]] += ocs
					else:
						temp[value + pair[1]] = ocs

		pairs = temp

	charCount = {}
	for pair in pairs:

		if pair[0] in charCount:
			charCount[pair[0]] += pairs[pair]
		else:
			charCount[pair[0]] = pairs[pair]

		if pair[1] in charCount:
			charCount[pair[1]] += pairs[pair]
		else:
			charCount[pair[1]] = pairs[pair]

	# Initial and last char in initial did not form 2 pairs like any other middle char
	charCount[initial[0]] += 1
	charCount[initial[-1]] += 1

	# Need / 2 to get the correct value of that char since any middle char will be count twice
	counts = [c[1] // 2 for c in charCount.items()]

	sol = max(counts) - min(counts)
	print(sol)

part2()