import itertools

raw_data = open('./data/day8.data.txt', 'r').read().split('\n')

def part1():

	data = [line[line.index('|') + 2:].split(' ') for line in raw_data]

	valid_len = [2, 4, 3, 7] # Number of segments to represent 1, 4, 7, 8 in 7 segment display

	total = 0

	for line in data:

		for digit in line:

			if len(digit) in valid_len:

				total += 1

	print(total)

part1()

def part2():

	data = [[sorted(line[:line.index("|") - 1].split(" ")), line[line.index("|") + 2:].split(" ")] for line in raw_data]

	valid_comb = [
		'abcefg',
		'cf',
		'acdeg',
		'acdfg',
		'bcdf',
		'abdfg',
		'abdefg',
		'acf',
		'abcdefg',
		'abcdfg'
	]

	digits = sorted(valid_comb)
	digits = tuple(digits)

	total = 0

	for line in data:

		for comb in itertools.permutations("abcdefg"):

			# Get relations between letters to remap each clue

			key = {}
			for c in "abcdefg":
				key[c] = comb["abcdefg".index(c)]

			new_clues = [] * 10

			# Pass actual clues to correct mapped ones
			for clue in line[0]:
				x = ""
				for char in clue:
					x += key[char]
				x = "".join(sorted(x))
				new_clues.append(x)

			new_clues.sort()

			if tuple(new_clues) == digits:

				n = []
				for d in line[1]:
					x = ""
					for char in d:
						x += key[char]
					x = "".join(sorted(x))
					n.append(valid_comb.index(x))

				total += int("".join([str(i) for i in n]))

				break

	print(total)

part2()