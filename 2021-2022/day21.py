from collections import Counter
from itertools import product
from functools import cache

input_data = open('./data/day21.data.txt', 'r').read().split("\n")

p1 = int(input_data[0].split(" ")[-1])
p2 = int(input_data[1].split(" ")[-1])

def play1(p1pos, p2pos, p1score = 0, p2score = 0, i = 0):

	if p2score >= 1000:
		return i * p1score
	p1pos = (p1pos + 3 * i + 5) % 10 + 1
	return play1(p2pos, p1pos, p2score, p1score + p1pos, i + 3)

def part1():

	print(play1(p1, p2))

part1()

roll_counts = Counter(map(sum, product((1, 2, 3), repeat=3)))

@cache
def play2(p1pos, p2pos, p1score=0, p2score=0):
	if p2score >= 21:
		return 1
	return sum(count * play2(
			p2pos,
			new_p1pos := (p1pos + roll - 1) % 10 + 1,
			p2score,
			p1score + new_p1pos,
		).conjugate() * 1j
		for roll, count in roll_counts.items()
	)

def part2():

	res = play2(p1, p2)
	print(int(max(res.real, res.imag)))

part2()
