from input_handler import convert_input


def score_winning_numbers(data):
	total_sum = 0

	for line in data:
		print(line)
		winning_nums = 0
		card_value = 0
		for wn in line[1][0]:
			if wn in line[1][1]:
				winning_nums += 1
				print(f'   Winning number found! {winning_nums} winning numbers so far...')
				if winning_nums == 1:
					card_value = 1
				else:
					card_value *= 2
				print(f'      Card value: {card_value}')
		total_sum += card_value

	return total_sum


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = score_winning_numbers(data)

	return total_sum


total = main()
print(f'\nTotal: {total}')
