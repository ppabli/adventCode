data = open('day1.data.txt', 'r').read().split('\n')

def part1():
	incremnt = 0
	for i in range(len(data) - 2):
		if int(data[i]) < int(data[i + 1]):
			incremnt += 1
	print(incremnt)

part1()

def part2():
	incremnt = 0
	for i in range(0, len(data) - 4, 1):
		sum1 = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
		sum2 = int(data[i + 1]) + int(data[i + 2]) + int(data[i + 3])
		if sum1 < sum2:
			incremnt += 1
	print(incremnt)

part2()