from input_handler import convert_input


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	for line in data:
		print(line)

	return total_sum


total = main()
print(f'Total: {total}')
