from input_handler import convert_input


def process_line(line):
	new_line = []
	for i in range(len(line)):
		if i < len(line) - 1:
			new_line.append(line[i + 1] - line[i])
	return new_line


def process_line_set(line_set):
	zero_line = line_set.pop(-1)
	# print(f'Zero line: {zero_line}')
	# print(f'Line set: {line_set}')
	for i in range((len(line_set)) - 1, -1, -1):
		if i > 0:
			temp = line_set[i - 1]
			next_number = line_set[i - 1][0] - line_set[i][0]
			line_set[i - 1] = [next_number]
			for j in temp:
				line_set[i - 1].append(j)
	# print(line_set)
	return line_set[0][0]


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	for line in data:
		line_set = [line]
		print(line)
		new_line = process_line(line)
		# print(new_line)
		for _ in range(len(line)):
			line_set.append(new_line)
			if len(set(new_line)) == 1 and 0 in set(new_line):
				# print(len(line_set))
				break
			new_line = process_line(new_line)
			# print(new_line)
		# print(line_set)
		next_number = process_line_set(line_set)
		print(f'Next in original sequence: {next_number}\n')
		total_sum += next_number

	return total_sum


total = main()
print(f'Total: {total}')
