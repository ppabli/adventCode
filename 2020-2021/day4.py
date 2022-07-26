import re

raw_data = open('./data/day4.data.txt', 'r').read().split('\n\n')

passports = []
for block in raw_data:
	parsed = re.findall(r'(\w+):(\S+)', block)
	passports.append({m[0]: m[1] for m in parsed})

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def includeAllFields(passport):

	return not any(required - passport.keys())

def part1():

	print(sum(map(includeAllFields, passports)))

part1()

def valid_data(passport):

	try:

		byr = int(passport['byr'])
		if not 1920 <= byr <= 2002:
			return False

		iyr = int(passport['iyr'])
		if not 2010 <= iyr <= 2020:
			return False

		eyr = int(passport['eyr'])
		if not 2020 <= eyr <= 2030:
			return False

		hgt = passport['hgt']
		match = re.match(r'(\d+)(cm|in)', hgt)
		height, unit = match[1], match[2]
		if unit == 'cm':
			if not 150 <= int(height) <= 193:
				return False
		elif unit == 'in':
			if not 59 <= int(height) <= 76:
				return False
		else:
			return False

		hcl = passport['hcl']
		if hcl[0] != '#' or len(hcl) != 7:
			return False
		int(hcl[1:], 16)
		ecl = passport['ecl']
		if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
			return False
		pid = passport['pid']
		if not pid.isdigit() or len(pid) != 9:
			return False

		return True

	except:

		return False

def part2():

	print(sum(map((includeAllFields and valid_data), passports)))

part2()