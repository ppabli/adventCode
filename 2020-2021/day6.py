raw_data = open('./data/day6.data.txt', 'r').read()

groups = raw_data.split("\n\n")

def part1():

	print(sum(len(set(g.replace('\n', ''))) for g in groups))

part1()

def part2():

	print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))

part2()
