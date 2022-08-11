raw_data = open('./data/day8.data.txt', 'r').read().split("\n")

instructions = [w.split()[0] for w in raw_data]
values = [int(w.split()[1]) for w in raw_data]

def run(instructions, values):

	i = 0
	acc = 0
	seen = set()

	while True:

		if i in seen:

			return (False, acc)

		elif i == len(raw_data):

			return (True, acc)

		seen.add(i)

		inst = instructions[i]
		value = values[i]

		if inst == 'acc':
			acc += value
		if inst == 'jmp':
			i += value
		else:
			i += 1

def part1():

	print(run(instructions, values)[1])

part1()

def part2():

	change = (i for i, x in enumerate(instructions) if x in ("nop", "jmp"))

	for i in change:

		new_ins = list(instructions)
		new_ins[i] = 'jmp' if instructions[i] == 'nop' else 'nop'

		ended, acc = run(new_ins, values)

		if ended:

			print(acc)

part2()
