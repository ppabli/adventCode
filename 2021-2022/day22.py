import re
import numpy as np
from math import prod

input_data = open('./data/day22.data.txt', 'r').read().split("\n")

boxes = [list(map(int, re.findall("-?\d+", x))) for x in input_data]
switches = [l.split()[0] == "on" for l in input_data]

switched_boxes = list(zip(switches, boxes))

def part1():

	a = np.zeros((100, 100, 100))

	for switch, box in switched_boxes:
		box = np.array(box) + 50
		a[box[0] : box[1] + 1, box[2] : box[3] + 1, box[4] : box[5] + 1] = switch

	print(int(a.sum()))

part1()

def intersection(boxes):

	x1, x2 = max(x[0] for x in boxes), min(x[1] for x in boxes)
	y1, y2 = max(x[2] for x in boxes), min(x[3] for x in boxes)
	z1, z2 = max(x[4] for x in boxes), min(x[5] for x in boxes)
	if x1 <= x2 and y1 <= y2 and z1 <= z2:
		return (x1, x2, y1, y2, z1, z2)

def volume(box):
	return prod(box[i + 1] - box[i] + 1 for i in (0, 2, 4))

def part2():

	seen = []

	for switch, box in switched_boxes:
		seen += [(overlap, -sign) for seen_box, sign in seen if (overlap := intersection([box, seen_box]))]
		if switch:
			seen.append((box, 1))

	print(sum(sign * volume(box) for box, sign in seen))

part2()