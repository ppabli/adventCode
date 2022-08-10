from heapq import heappop, heappush

room_loc = {"A": 2, "B": 4, "C": 6, "D": 8}
mults = {"A": 1, "B": 10, "C": 100, "D": 1000}

def home_is_free(state, home):
	count = len(state) // 4
	proper_home = {x: range(i * count, (i + 1) * count) for i, x in enumerate("ABCD")}
	return not any(
		piece[0] == home and i not in proper_home[home] for i, piece in enumerate(state)
	)


def replace_piece(state, new_piece, i):
	new_state = list(state)
	new_state[i] = new_piece
	return tuple(new_state)


def move_to_corridor(state, to_check, loc, position):
	for j in to_check:
		if ("corr", j) in state:
			return
		if j not in room_loc.values():
			yield ("corr", j), abs(j - room_loc[loc]) + position + 1


def action_single_piece(state, i, home):
	piece = state[i]
	loc, position = piece
	can_move_to_home = home_is_free(state, home)

	if loc in "ABCD" and any((loc, j) in state for j in range(position)):
		return

	if loc == home and can_move_to_home:
		return

	if loc in "ABCD":
		for to_check in (
			range(room_loc[loc] - 1, -1, -1),
			range(room_loc[loc] + 1, 11),
		):
			yield from move_to_corridor(state, to_check, loc, position)

	if can_move_to_home:
		first_available = max(
			j for j in range(len(state) // 4) if (home, j) not in state
		)
	
		if loc in "ABCD":
			corr_to_check = range(
				min(room_loc[loc], room_loc[home]),
				max(room_loc[loc], room_loc[home]) + 1,
			)
			distance = (
				abs(room_loc[loc] - room_loc[home]) + first_available + position + 2
			)
		else:
			corr_to_check = set(
				range(min(position, room_loc[home]), max(position, room_loc[home]) + 1)
			) - {position}
			distance = abs(position - room_loc[home]) + first_available + 1
		if not any(("corr", j) in state for j in corr_to_check):
			yield (home, first_available), distance


def actions(state, homes):
	"""For a given state, generates all states that can be reached from here."""
	for i in range(len(state)):
		home = homes[i]
		mult = mults[home]
		for new_piece, length in action_single_piece(state, i, home):
			yield replace_piece(state, new_piece, i), mult * length


def solve(start_state):
	q = [(0, start_state)]
	homes = "".join(x * (len(start_state) // 4) for x in "ABCD")
	visited = set()
	while q:
		dist, state = heappop(q)
		if state in visited:
			continue
		if "".join(s[0] for s in state) == homes:
			print(dist)
			break
		visited.add(state)
		for new_state, new_dist in actions(state, homes):
			heappush(q, (dist + new_dist, new_state))

def part1():

	##############
	#...........#
	###B#D#C#A###
	  #C#D#B#A#
	  #########

	solve(
		(
			("D", 0),
			("D", 1),

			("A", 0),
			("C", 1),

			("A", 1),
			("C", 0),

			("B", 0),
			("B", 1),
		)
	)

part1()

def part2():

	##############
	#...........#
	###B#D#C#A###
	  #D#C#B#A#
	  #D#B#A#C#
	  #C#D#B#A#
	  #########

	solve(
		(

			("C", 2),
			("D", 0),
			("D", 1),
			("D", 3),

			("A", 0),
			("B", 2),
			("C", 1),
			("C", 3),

			("A", 3),
			("B", 1),
			("C", 0),
			("D", 2),

			("A", 1),
			("A", 2),
			("B", 0),
			("B", 3),
		)
	)

part2()