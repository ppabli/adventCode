import re

raw_data = open('./data/day5.data.txt', 'r').read().split('\n')

def convert_binary(w):
	w = re.sub('[FL]', '0', w)
	w = re.sub('[BR]', '1', w)
	return int(w, 2)

def part1():

	print(max(map(convert_binary, raw_data)))

part1()

def part2():

	ids = list(map(convert_binary, raw_data))

	for id in sorted(ids):

		if id + 1 not in ids and id + 2 in ids:

			print(id + 1)

			break

part2()
