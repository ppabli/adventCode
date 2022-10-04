raw_data = open('./data/day18.data.txt', 'r').read().split("\n")

def calc(s, order):
	if "(" in s:
		openp = 0
		start = s.index("(")
		for i in range(start, len(s)):
			if s[i] == "(":
				openp += 1
			elif s[i] == ")":
				openp -= 1
			if openp == 0:
				break
		return calc(s[:start] + calc(s[start + 1 : i], order) + s[i + 1 :], order)

	else:
		grams = s.split(" ")
		total = 0
		for ops in order:
			i = 1
			while i < len(grams):
				if grams[i] in ops:
					grams = (grams[: i - 1] + [str(eval(" ".join(grams[i - 1 : i + 2])))] + grams[i + 2 :])
				else:
					i += 2
		return grams[0]

def part1():

	res = sum([int(calc(l, ["+*"])) for l in raw_data])
	print(res)

part1()

def part2():

	res = sum([int(calc(l, ["+", "*"])) for l in raw_data])
	print(res)

part2()