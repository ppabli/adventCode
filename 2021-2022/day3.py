data = open('day3.data.txt', 'r').read().split('\n')

length = len(data[0])

def dataSummary(data, n, moreCommon = True):

	ones = 0
	ceros = 0

	for i in range(len(data)):
		if data[i][n] == '1':
			ones += 1
		else:
			ceros += 1

	if ones > ceros:
		if moreCommon:
			return '1'
		else:
			return '0'
	elif ceros > ones:
		if moreCommon:
			return '0'
		else:
			return '1'
	else:
		if moreCommon:
			return '1'
		else:
			return '0'

def filterData(data, n, value):

	if len(data) == 1:
		return data

	newData = []

	for i in range(len(data)):
		if data[i][n] == value:
			newData.append(data[i])

	return newData

def part1():

	gamma = ''
	epsilon = ''

	for i in range(length):
		gamma += str(dataSummary(data, i))
		epsilon += str(dataSummary(data, i, False))

	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)

	print(gamma, epsilon, gamma * epsilon)

part1()

def part2():

	oxygenData = data
	co2Data = data

	for i in range(length):

		oxygenData = filterData(oxygenData, i, dataSummary(oxygenData, i))
		co2Data = filterData(co2Data, i, dataSummary(co2Data, i, False))

	oxygenData = int(oxygenData[0], 2)
	co2Data = int(co2Data[0], 2)

	print(oxygenData, co2Data, oxygenData * co2Data)

part2()