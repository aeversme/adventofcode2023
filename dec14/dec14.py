from input_handler import convert_input


class Node:
	def __init__(self, pos, row, col, char):
		self.pos = pos
		self.row = row
		self.col = col
		self.char = char

	def __repr__(self):
		return f'Pos {self.pos} row: {self.row} col: {self.col} char: {self.char}'


def convert_to_nodes(data):
	data_nodes = []

	for a in range(len(data)):
		new_line = []
		print(data[a])
		for b in range(len(data[0])):
			new_node = Node((a, b), a, b, data[a][b])
			# print(new_node)
			new_line.append(new_node)
		data_nodes.append(new_line)

	return data_nodes


def move_node_north(node, data_nodes):
	row = node.row
	col = node.col
	# move_to_row = row
	print(node)
	for i in range(len(data_nodes[:row]), 0, -1):
		if i > 0:
			print(data_nodes[i - 1][col])
			if data_nodes[i - 1][col].char != '.':
				print('   Can\'t move')
				return
			move_to_row = row - i
			print(f'   Move to row {move_to_row}')
			data_nodes[i - 1][col].char = 'O'
			data_nodes[i][col].char = '.'
			# print(data_nodes[row - 1])
			# print(data_nodes[row])
	return


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	data_nodes = convert_to_nodes(data)

	for i in range(1, len(data_nodes)):
		for node in data_nodes[i]:
			if node.char == 'O':
				move_node_north(node, data_nodes)

	new_data = []

	for line in data_nodes:
		new_line = ''
		for n in line:
			new_line += n.char
		new_data.append(new_line)

	for i in range(len(new_data), 0, -1):
		count = 0
		line = new_data[abs(len(new_data) - i)]
		print(line)
		for char in line:
			if char == 'O':
				count += 1
		total_sum += count * i

	return total_sum


total = main()
print(f'Total: {total}')
