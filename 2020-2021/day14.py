raw_data = open('./data/day14.data.txt', 'r').read().split('\n')

def part1():

	mem = {}

	for inst in raw_data:
		if inst.startswith("mask"):
			mask_in = inst.split(" ")[2]
			m_or = int(mask_in.replace("X", "0"), 2)
			m_and = int(mask_in.replace("X", "1"), 2)
		elif inst.startswith("mem"):
			idx = int(inst.split("[")[1].split("]")[0])
			val = int(inst.split(" ")[2])
			mem[idx] = (val & m_and) | m_or

	print(sum([v for k,v in mem.items()]))

part1()

def get_indexes(mask):
	try:
		firstx = mask.index("X")
		return get_indexes(mask[:firstx] + "0" + mask[firstx + 1 :]) + get_indexes(mask[:firstx] + "1" + mask[firstx + 1 :])
	except ValueError:
		return [int(mask, 2)]

def part2():

	mem = {}

	for inst in raw_data:
		if inst.startswith("mask"):
			mask = inst.split(" ")[2]
		elif inst.startswith("mem"):
			idx = int(inst.split("[")[1].split("]")[0])
			val = int(inst.split(" ")[2])
			idx_mask = ""
			for m, i in zip(mask, f"{idx:036b}"):
				if m == "0":
					idx_mask += i
				elif m == "1" or m == "X":
					idx_mask += m
				else:
					assert False
			idxs = get_indexes(idx_mask)
			for idx in idxs:
				mem[idx] = val

	print(sum([v for k,v in mem.items()]))

part2()