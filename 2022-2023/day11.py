data = open('./data/day11.data.txt', 'r').read().split('\n\n')

def generateMonkeys():

	monkeys = []

	lcd = 1

	for monkey in data:

		monkeyLines = monkey.split('\n')

		items = list(map(int, monkeyLines[1].split(':')[1].split(',')))
		operation = monkeyLines[2].split(' = ')[1]
		testValue = int(monkeyLines[3].split('by ')[1])
		trueMonkey = int(monkeyLines[4][-1])
		falseMonkey = int(monkeyLines[5][-1])

		monkey = {

			'items': items,
			'iterations': 0,
			'operation': operation,
			'test': testValue,
			'testTrue': trueMonkey,
			'testFalse': falseMonkey,

		}

		monkeys.append(monkey)

		lcd *= testValue

	return monkeys, lcd


def part1():

	monkeys, _ = generateMonkeys()

	for turn in range(20):

		for monkey in monkeys:

			for item in range(len(monkey['items'])):

				monkey['iterations'] += 1

				item = monkey['items'].pop(0)

				old = item
				val = eval(monkey['operation'])

				worryValue = val // 3

				if worryValue % monkey['test'] == 0:

					monkeys[monkey['testTrue']]['items'].append(worryValue)

				else:

					monkeys[monkey['testFalse']]['items'].append(worryValue)

	finalIterations = []
	for monkey in monkeys:

		finalIterations.append(monkey['iterations'])

	finalIterations.sort(reverse=True)

	print(finalIterations[0] * finalIterations[1])

part1()

def part2():

	monkeys, lcd = generateMonkeys()

	for turn in range(10000):

		for monkey in monkeys:

			for item in range(len(monkey['items'])):

				monkey['iterations'] += 1

				item = monkey['items'].pop(0)

				old = item
				worryValue = eval(monkey['operation'])

				worryValue %= lcd

				if worryValue % monkey['test'] == 0:

					monkeys[monkey['testTrue']]['items'].append(worryValue)

				else:

					monkeys[monkey['testFalse']]['items'].append(worryValue)


	finalIterations = []
	for monkey in monkeys:

		finalIterations.append(monkey['iterations'])

	finalIterations.sort(reverse = True)

	print(finalIterations[0] * finalIterations[1])

part2()