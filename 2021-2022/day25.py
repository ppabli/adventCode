from itertools import count

input_data = open('./data/day25.data.txt', 'r').read().split("\n")

n = len(input_data)
m = len(input_data[0])

def step(rights, downs):
	nr = set()
	nd = set()
	to_check = rights | downs
	for x, y in rights:
		new_loc = (x, (y + 1) % m)
		nr.add((x, y) if new_loc in to_check else new_loc)
	to_check = nr | downs
	for x, y in downs:
		new_loc = ((x + 1) % n, y)
		nd.add((x, y) if new_loc in to_check else new_loc)
	return nr, nd

def part1():

	rights = {(i, j) for i in range(n) for j in range(m) if input_data[i][j] == '>'}
	downs = {(i, j) for i in range(n) for j in range(m) if input_data[i][j] == 'v'}

	for c in count(1):
		new_rights, new_downs = step(rights, downs)
		if rights == new_rights and downs == new_downs:
			print(c)
			break
		rights = new_rights
		downs = new_downs

part1()