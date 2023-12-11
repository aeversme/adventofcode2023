from input_handler import convert_input

pipe_dict = {
		# difference: [next, left, right]
		'|': {
			(-1, 0): [(-1, 0), [(0, -1)], [(0, 1)]],
			(1, 0): [(1, 0), [(0, 1)], [(0, -1)]]
		},
		'-': {
			(0, -1): [(0, -1), [(1, 0)], [(-1, 0)]],
			(0, 1): [(0, 1), [(-1, 0)], [(1, 0)]]
		},
		'L': {
			(0, -1): [(-1, 0), [(1, 0), (0, -1)], [(0, 1)]],
			(1, 0): [(0, 1), [], [(0, -1), (1, 0)]]
		},
		'J': {
			(0, 1): [(-1, 0), [], [(1, 0), (0, 1)]],
			(1, 0): [(0, -1), [(0, 1), (1, 0)], [(0, -1)]]
		},
		'7': {
			(0, 1): [(1, 0), [(-1, 0), (0, 1)], []],
			(-1, 0): [(0, -1), [], [(0, 1), (-1, 0)]]
		},
		'F': {
			(-1, 0): [(0, 1), [(0, -1), (-1, 0)], []],
			(0, -1): [(1, 0), [], [(0, -1), (-1, 0)]]
		}
	}


class Node:
	def __init__(self, coords, pipe_type, is_start=False):
		self.coords = coords
		self.next_node = None
		self.parent_node = None
		self.is_start = is_start
		self.pipe_type = pipe_type

	def __repr__(self):
		return f'Node: {self.coords}; type: {self.pipe_type}, parent: {self.parent_node},' \
			   f' next: {self.next_node}, is start: {self.is_start}'

	def insert_next(self, next_coords):
		self.next_node = next_coords

	def insert_parent(self, parent_coords):
		self.parent_node = parent_coords


def evaluate_surrounding_pos(node, pipes):
	difference = (node.coords[0] - node.parent_node[0], node.coords[1] - node.parent_node[1])
	for k, v in pipe_dict.items():
		if node.pipe_type == k:
			left_list = pipe_dict[node.pipe_type][difference][1]
			right_list = pipe_dict[node.pipe_type][difference][2]
			if left_list:
				for le in left_list:
					# print(le)
					# print(le[0])
					# print(le[1])
					# print(pipes[node.coords[0] + le[0]][node.coords[1] + le[1]])
					if pipes[node.coords[0] + le[0]][node.coords[1] + le[1]] == '.':
						pipes[node.coords[0] + le[0]] = pipes[node.coords[0] + le[0]][:node.coords[1] + le[1]] + '0' + pipes[node.coords[0] + le[0]][node.coords[1] + le[1] + 1:]
						# print(pipes[node.coords[0] + le[0]])
			if right_list:
				for ri in right_list:
					if pipes[node.coords[0] + ri[0]][node.coords[1] + ri[1]] == '.':
						pipes[node.coords[0] + ri[0]] = pipes[node.coords[0] + ri[0]][:node.coords[1] + ri[1]] + '1' + pipes[node.coords[0] + ri[0]][node.coords[1] + ri[1] + 1:]
	return pipes


def find_start_coords(pipes):
	coordinates = []
	for i in range(len(pipes)):
		for j in range(len(pipes[0])):
			if pipes[i][j] == 'S':
				coordinates = (i, j)
	return coordinates


def find_first_path(pipes, node):
	coords = node.coords
	for r in range(-1, 2):
		for c in range(-1, 2):
			if (r == -1 or r == 1) and c != 0:
				continue
			next_pipe = pipes[coords[0] + r][coords[1] + c]
			if next_pipe == '.':
				continue
			next_coords = (coords[0] + r, coords[1] + c)
			difference = (next_coords[0] - coords[0], next_coords[1] - coords[1])

			# print(next_pipe)
			# print(difference)

			if next_pipe != pipes[coords[0]][coords[1]]:
				for k, v in pipe_dict[next_pipe].items():
					if k == difference:
						# next_coords = (coords[0] + r, coords[1] + c)
						new_node = Node(next_coords, next_pipe)
						new_node.parent_node = coords
						node.next_node = next_coords
						print(f'Path start found!\n   Step 01: {new_node}')
						return new_node


def find_next_pipe(pipes, node):
	next_coords = ()
	next_node = Node(next_coords, '')
	difference = (node.coords[0] - node.parent_node[0], node.coords[1] - node.parent_node[1])
	for k, v in pipe_dict.items():
		if k == node.pipe_type:
			for d, n in v.items():
				if d == difference:
					goto = n[0]
					next_coords = (node.coords[0] + goto[0], node.coords[1] + goto[1])
					node.next_node = next_coords
					next_node.coords = next_coords
					next_node.pipe_type = pipes[next_coords[0]][next_coords[1]]
					next_node.parent_node = node.coords
	# print(f'Difference is {difference}, next pipe is {next_node.pipe_type} {next_node.coords}')
	return next_node


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	pipes = convert_input(i_raw)

	total_sum = 0

	# for line in pipes:
	# 	print(line)

	start_node = Node(find_start_coords(pipes), 'S', is_start=True)
	print(f'Start found!\n   Step 0: {start_node}')

	pipe_map = [start_node]
	new_node = find_first_path(pipes, start_node)
	pipe_map.append(new_node)

	for x in range(100000):
		new_node = find_next_pipe(pipes, new_node)

		if new_node.coords == start_node.coords:
			print(f'Map complete. There are {len(pipe_map)} nodes in the map.\nThe farthest node is {len(pipe_map) // 2} steps away.')
			break
		else:
			print(f'   Step {x + 2}: {new_node}')
			pipe_map.append(new_node)

	for g in range(len(pipes)):
		for h in range(len(pipes[0])):
			pos = (g, h)
			# print(f'Checking position {pos}')
			is_node = False
			for node in pipe_map:
				# print(f'   Checking against node {node.coords}...')
				if pos == node.coords:
					is_node = True
					break
			if not is_node:
				pipes[g] = pipes[g][:h] + '.' + pipes[g][h + 1:]

	for n in range(1, len(pipe_map)):
		pipes = evaluate_surrounding_pos(pipe_map[n], pipes)

	pipes.pop(-1)
	pipes.pop(0)

	original_pipes = []
	for line in pipes:
		new_line = line[1:-1]
		original_pipes.append(new_line)

	for line in original_pipes:
		print(line)

	pipes = original_pipes

	possibles = ['0', '1']

	outside = ''
	outside_found = False
	for t in range(len(pipes)):
		for s in range(len(pipes[0])):
			if pipes[t][s] in possibles:
				outside = pipes[t][s]
				outside_found = True
				print(f'Outside: {outside}')
				break
		if outside_found:
			break

	for t in range(1, len(pipes) - 1):
		most_recent = ''
		for s in range(1, len(pipes[0]) - 1):
			current = pipes[t][s]
			if current in possibles:
				most_recent = current
				if current != outside:
					total_sum += 1
			if current == '.' and most_recent:
				if most_recent != outside:
					total_sum += 1

	return total_sum


total = main()
print(f'Total: {total}')
