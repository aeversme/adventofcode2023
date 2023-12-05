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


def count_winning_cards(data):
	card_dict = {}
	for c in range(len(data)):
		card_dict[c + 1] = 1

	for card in data:
		print(card)
		card_number = card[0]

		winning_nums = 0
		for wn in card[1][0]:
			if wn in card[1][1]:
				winning_nums += 1
		print(f'   {winning_nums} winning numbers for card {card_number}...')

		for i in range(card_number + 1, card_number + winning_nums + 1):
			card_dict[i] += card_dict[card_number]

		print(card_dict)

	return card_dict


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	# total_sum = score_winning_numbers(data)

	total_sum = 0

	card_dict = count_winning_cards(data)
	for k, v in card_dict.items():
		total_sum += v

	return total_sum


total = main()
print(f'\nTotal: {total}')
