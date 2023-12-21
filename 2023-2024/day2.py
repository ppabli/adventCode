data = open('./data/day2.data.txt', 'r').read().strip().split('\n')

def part1():

	gameData = {
		'red': 12,
		'green': 13,
		'blue': 14,
	}

	total = 0

	for line in data:

		id, sets = line.split(':')
		id = int(id.split(" ")[1])

		valid = True

		for gameSet in sets.split("; "):

			for part in gameSet.split(", "):

				value, color = part.strip().split(" ")
				value = int(value)

				if color not in gameData or value > gameData[color]:

					valid = False
					break

			if not valid:

				break

		if valid:

			total += id

	print(total)

part1()

def part2():

	total = 0

	for line in data:

		lineData = {
			'red': 0,
			'green': 0,
			'blue': 0,
		}

		id, sets = line.split(':')
		id = int(id.split(" ")[1])

		for gameSet in sets.split("; "):

			for part in gameSet.split(", "):

				value, color = part.strip().split(" ")
				value = int(value)

				lineData[color] = max(lineData[color], value)

		total += lineData['red'] * lineData['green'] * lineData['blue']

	print(total)

part2()
