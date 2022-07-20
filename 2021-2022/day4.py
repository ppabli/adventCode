import numpy as np

data = open('day4.data.txt', 'r').read().split('\n')

numbers = [int(i) for i in data[0].split(',')]

boards = []

size = 5

for x in range(2, len(data), size + 1):

	board = []

	for y in range(size):

		line = data[x + y]

		lineValues = []
		lineNumbers = line.split(' ')

		while '' in lineNumbers:
			lineNumbers.remove('')

		for n in lineNumbers:

			lineValues.append(int(n))

		board.append(lineValues)

	boards.append(board)


start = size

def getLine(board, numbers):

	validLine = []

	#Check y line

	for i in range(size):

		if (set(board[i]).issubset(set(numbers))):

			validLine = set(board[i])

			break

	#Check x line

	for i in range(size):

		if (set([row[i] for row in board]).issubset(set(numbers))):

			validLine = set([row[i] for row in board])

			break


	return validLine

def getUnmarked(board, validNumbers):

	unmarked = []

	for i in range(size):

		for j in range(size):

			if (board[i][j] not in validNumbers):

				unmarked.append(board[i][j])

	return unmarked


def part1():


	validLine = []


	for n in range(0, len(numbers) - size + 1):

		numbersToCheck = numbers[0 : start + n]

		for board in range(0, len(boards)):

			validLine = getLine(boards[board], numbersToCheck)

			if validLine:

				break

		if validLine:

			print("Unmarked:", getUnmarked(boards[board], numbersToCheck))
			print("Last number:", numbersToCheck[-1], "| Winning line:", validLine, "| Score:", numbersToCheck[-1] * sum(getUnmarked(boards[board], numbersToCheck)))

			break


part1()

def part2():

	validLine = []
	winBoard = []
	winNumbersCheck = []

	removedBoards = []

	forceOut = False

	for n in range(0, len(numbers) - size + 1):

		numbersToCheck = numbers[0 : start + n]

		for board in range(0, len(boards)):

			if board in removedBoards:

				continue

			tempLine = getLine(boards[board], numbersToCheck)

			if len(tempLine) != 0 and (len(boards) - 1 == len(removedBoards)):

				validLine = tempLine
				winBoard = boards[board]
				winNumbersCheck = numbersToCheck

				forceOut = True

				break

			elif len(tempLine) != 0:

				removedBoards.append(board)
		
		if forceOut:

			break

	print("Unmarked:", getUnmarked(winBoard, winNumbersCheck))
	print("Last number:", winNumbersCheck[-1], "| Winning line:", validLine, "| Score:", winNumbersCheck[-1] * sum(getUnmarked(winBoard, winNumbersCheck)))

part2()