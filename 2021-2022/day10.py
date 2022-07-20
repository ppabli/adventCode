raw_data = open('day10.data.txt', 'r').read().split('\n')

open_pairs = ['(', '[', '<', "{"]
close_pairs = [')', ']', '>', "}"]

def part1():

	total = 0

	points = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}

	for line in raw_data:

		stack = []

		for char in line:

			if char in open_pairs:

				stack.append(char)

			else:

				if stack[-1] == open_pairs[close_pairs.index(char)]:

					stack.pop()

				else:

					# No valid
					total += points[char]

					# Just one failure per line
					break

	print(total)

part1()

def part2():

	scores = []

	for line in raw_data:

		valid = True
		points = {
			")": 1,
			"]": 2,
			"}": 3,
			">": 4
		}
		stack = []

		for char in line:

			if char in open_pairs:

				stack.append(char)

			else:

				if stack[-1] == open_pairs[close_pairs.index(char)]:

					stack.pop()

				else:

					valid = False
					break

		if valid:

			missing_characters = []

			while len(stack) > 0:

				missing_characters.append(close_pairs[open_pairs.index(stack[-1])])

				stack.pop()

			total = 0

			for char in missing_characters:

				total *= 5
				total += points[char]

			scores.append(total)

	scores.sort()

	print(scores[len(scores) // 2])

part2()