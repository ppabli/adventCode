data = open('./data/day5.data.txt', 'r').read().split('\n')

stacks = []
cols = 9
movementStart = 10

def generateInitial():

	global stacks

	stacks = []

	for x in range(cols):

		stacks.append([])

	for line in data[:cols]:

		startIndex = 0

		for part in range(cols):

			if (line[startIndex] == '['):

				stacks[part].append(line[startIndex + 1])

			startIndex += 4

	for x in range(cols):

		stacks[x].reverse()

def part1():

	generateInitial()

	for movement in data[movementStart:]:

		splitedLine = movement.split(' ')

		amount = int(splitedLine[1])
		f = int(splitedLine[3]) - 1
		t = int(splitedLine[5]) - 1

		for c in range(amount):

			ele = stacks[f].pop()
			stacks[t].append(ele)

	message = ''
	for x in range(cols):

		message += stacks[x].pop()

	print(message)

part1()

def part2():

	generateInitial()

	for movement in data[movementStart:]:

		splitedLine = movement.split(' ')

		amount = int(splitedLine[1])
		f = int(splitedLine[3]) - 1
		t = int(splitedLine[5]) - 1

		elements = stacks[f][len(stacks[f]) - amount:]

		for element in elements:

			stacks[f].pop()
			stacks[t].append(element)

	message = ''
	for x in range(cols):

		message += stacks[x].pop()

	print(message)

part2()