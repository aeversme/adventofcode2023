from input_handler import convert_input

# 5 of kind = set length 1
# 4 of kind - set length 2
# full house = set length 2
# 3 of kind = set length 3
# two pair = set length 3
# one pair = set length 4
# high card = set length 5


def hand_type(hand):
	cards = set(hand[0])
	if len(cards) == 1:
		return 'five'
	if len(cards) == 2:
		counts = []
		for card in cards:
			counts.append(hand[0].count(card))
		if 'J' in cards:
			return 'five'
		if 4 in counts:
			return 'four'
		return 'full'
	if len(cards) == 3:
		counts = []
		for card in cards:
			counts.append(hand[0].count(card))
		if 3 in counts:
			if 'J' in cards:
				return 'four'
			return 'three'
		else:
			if 'J' in cards:
				if hand[0].count('J') == 1:
					return 'full'
				if hand[0].count('J') == 2:
					return 'four'
			return 'two'
	if len(cards) == 4:
		if 'J' in cards:
			return 'three'
		return 'one'
	if len(cards) == 5:
		if 'J' in cards:
			return 'one'
		return 'high'


def order_hands(hand_list, card_number):
	print(hand_list)
	card_rank = 'J23456789TQKA'
	hand_order = [[], [], [], [], [], [], [], [], [], [], [], [], []]
	final_order = []
	for hand in hand_list:
		sorting_card = hand[0][card_number]
		card_index = card_rank.index(sorting_card)
		hand_order[card_index].append(hand)
	print(hand_order)
	for q in hand_order:
		if len(q) == 0:
			continue
		if len(q) == 1:
			final_order.append(q[0])
		else:
			other_list = order_hands(q, card_number + 1)
			for z in other_list:
				final_order.append(z)

	return final_order


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	print(data)

	hands = {
		'high': [],
		'one': [],
		'two': [],
		'three': [],
		'full': [],
		'four': [],
		'five': []
	}

	for hand in data:
		h_type = hand_type(hand)
		print(f'Hand: {hand}, type: {h_type}')
		hands[h_type].append(hand)

	hand_order = []

	for k, v in hands.items():
		print(k)
		hand_type_list = order_hands(v, 0)
		print(hand_type_list)
		for x in hand_type_list:
			hand_order.append(x)

	print(hand_order)

	for n in range(len(hand_order)):
		total_sum += hand_order[n][1] * (n + 1)

	return total_sum


total = main()
print(f'Total: {total}')
