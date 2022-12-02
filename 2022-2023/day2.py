data = open('./data/day2.data.txt', 'r').read().strip().split('\n')

def part1():

	pointsPerType = {

		'A': 1,
		'B': 2,
		'C': 3,
		'X': 1,
		'Y': 2,
		'Z': 3,
		'draft': 3,
		'win': 6,
		'lose': 0

	}

	totalPoints = 0

	for play in data:

		oponent, you = play.split(' ')

		pointsYou = pointsPerType[you]
		pointsOponent = pointsPerType[oponent]

		if (pointsYou - pointsOponent == 1 or (pointsYou == 1 and pointsOponent == 3)):

			totalPoints += pointsPerType['win'] + pointsYou

		elif (pointsYou - pointsOponent == 0):

			totalPoints += pointsPerType['draft'] + pointsYou

		else:

			totalPoints += pointsPerType['lose'] + pointsYou

	print(totalPoints)

part1()

def part2():

	# Rock
	# Paper
	# Scissors

	pointsPerType = {

		'A': 1,
		'B': 2,
		'C': 3,

		'draft': 3,
		'win': 6,
		'lose': 0

	}

	totalPoints = 0

	for play in data:

		oponent, you = play.split(' ')

		pointsOponent = pointsPerType[oponent]

		if (you == 'X'):

			youPoints = pointsOponent - 1
			if (youPoints == 0):
				youPoints = 3

			totalPoints += pointsPerType['lose'] + youPoints

		elif (you == 'Y'):

			totalPoints += pointsPerType['draft'] + pointsOponent

		else:

			totalPoints += pointsPerType['win'] + (pointsOponent % 3) + 1

	print(totalPoints)

part2()