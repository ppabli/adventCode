from functools import reduce
from itertools import product
from math import prod

raw_data = open('./data/day18.data.txt', 'r').read().split("\n")

def make_dict(x, d=None, index=1):
	if d is None:
		d = {}
	if isinstance(x, int):
		d[index] = x
	else:
		make_dict(x[0], d, 2 * index)
		make_dict(x[1], d, 2 * index + 1)
	return d

def action(d):
	keys = sorted(d, key=bin)
	first, *_, last = keys
	# Explode
	for i in range(len(keys)):
		if keys[i] >= 32:
			k1, k2 = keys[i : i + 2]
			if k1 != first:
				d[keys[i - 1]] += d[k1]
			if k2 != last:
				d[keys[i + 2]] += d[k2]
			del d[k1]
			del d[k2]
			d[k1 // 2] = 0
			return True
	# Split
	for k in keys:
		v = d[k]
		if v >= 10:
			d[2 * k] = v // 2
			d[2 * k + 1] = v - v // 2
			del d[k]
			return True
	return False

def simplify(d):
	while action(d):
		pass
	return d

def add(d1, d2):
	return simplify(
		{int("10" + bin(k)[3:], 2): v for k, v in d1.items()}
		| {int("11" + bin(k)[3:], 2): v for k, v in d2.items()}
	)

def magnitude(d):
	return sum(v * prod(3 - int(digit) for digit in bin(k)[3:]) for k, v in d.items())

def part1():

	dicts = list(map(make_dict, map(eval, raw_data)))
	print(magnitude(reduce(add, dicts)))

part1()

def part2():

	dicts = list(map(make_dict, map(eval, raw_data)))
	print(max(magnitude(add(d1, d2)) for d1, d2 in product(dicts, dicts) if d1 != d2))

part2()