from input_handler import convert_input


digit_map = [
	['one', 3, '1'],
	['two', 3, '2'],
	['three', 5, '3'],
	['four', 4, '4'],
	['five', 4, '5'],
	['six', 3, '6'],
	['seven', 5, '7'],
	['eight', 5, '8'],
	['nine', 4, '9']
]


first_letters = ['o', 't', 'f', 's', 'e', 'n']


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)
	# for line in data:
	# 	print(line)

	number_list = []
	line_num = 0

	for line in data:
		line_num += 1
		# print(line)
		line_numbers = []
		for i in range(len(line)):
			if line[i].isdigit():
				# print(f'Index {i}: digit found: {line[i]}')
				line_numbers.append(line[i])
				# print(f'         Number list for this line: {line_numbers}')
			else:
				char = line[i]
				# print(f'Index {i}: letter found: {char}')
				if char in first_letters:
					# print(f'   Letter {char} found in first letters')
					for item in digit_map:
						num_str = item[0]
						line_slice = line[i:i + item[1]]
						# print(f'      Item: {num_str}, slice: {line_slice}')
						if num_str == line_slice:
							# print('         Match found!')
							line_numbers.append(item[2])
							# print(f'         Number list for this line: {line_numbers}')

		# print(line_numbers)
		number_str = line_numbers[0] + line_numbers[-1]
		print(f'Line {line_num}: {line}; {line_numbers}; {number_str}')
		number_list.append(int(number_str))

	total = 0
	num_index = 0
	for num in number_list:
		num_index += 1
		if 9 < num < 100:
			total += num
		else:
			# print(num)
			print(f'******Warning, not a valid two-digit number! Index {num_index + 1}')

	return total


calibration_sum = main()
print(f'\nCalibration sum is: {calibration_sum}')
