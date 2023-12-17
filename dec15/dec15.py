from input_handler import convert_input


def hash_func(string):
	num = 0
	for char in string:
		num += ord(char)
		num *= 17
		num = num % 256
	return num


def find_lens_box(string):
	symbol = ''
	for char in string:
		if char == '=' or char == '-':
			symbol = char
	si = string.index(symbol)
	label = string[:si]
	box = hash_func(label)

	return label, box, symbol


def box_operation(string, label, box, symbol, box_dict):
	if symbol == '=':
		val = string[string.index(symbol) + 1:]
		if box_dict[box]:
			in_box = False
			for lens in box_dict[box]:
				if lens[0] == label:
					in_box = True
					li = box_dict[box].index(lens)
					new_list = box_dict[box][:li] + [[label, val]] + box_dict[box][li + 1:]
					box_dict[box] = new_list
					break
			if not in_box:
				box_dict[box].append([label, val])
		else:
			box_dict[box].append([label, val])
	else:
		if box_dict[box]:
			for lens in box_dict[box]:
				if lens[0] == label:
					li = box_dict[box].index(lens)
					box_dict[box].pop(li)

	return box_dict


def focus_power(box_list, box_num, lens):
	one_plus = box_num + 1
	slot_number = box_list.index(lens) + 1
	focal_length = int(lens[1])
	print(f'   Lens: {lens}, one+: {one_plus}, slot: {slot_number}, focal: {focal_length}')
	return one_plus * slot_number * focal_length


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	box_dict = {}
	for i in range(len(data)):
		box_dict[i] = []

	for string in data:
		# part 1
		# result = hash_func(string)
		# print(f'{string}: {result}')
		# total_sum += result

		# part 2
		label, box, symbol = find_lens_box(string)
		# print(f'{string}: label {label}, box {box}, symbol {symbol}')
		box_dict = box_operation(string, label, box, symbol, box_dict)
		# print(box_dict)

	for i in range(len(box_dict)):
		box = box_dict[i]
		if box:
			print(f'Box: {box}')
			for lens in box:
				power = focus_power(box, i, lens)
				print(f'      Lens power: {power}')
				total_sum += int(power)
		else:
			continue

	return total_sum


total = main()
print(f'Total: {total}')
