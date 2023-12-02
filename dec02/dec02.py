from input_handler import convert_input


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	id_sum = 0

	for game in data:
		valid_game = True
		print(game)
		for subset in game[1]:
			if not valid_game:
				break
			print(f'   Subset: {subset}')
			for color in subset:
				if not valid_game:
					break
				# print(f'      Color: {color}')
				if color[1] == 'red' and int(color[0]) > 12:
					print(f'         Too many reds in {subset}.')
					valid_game = False
					break
				elif color[1] == 'green' and int(color[0]) > 13:
					print(f'         Too many greens in {subset}.')
					valid_game = False
					break
				elif color[1] == 'blue' and int(color[0]) > 14:
					print(f'         Too many blues in {subset}.')
					valid_game = False
					break
		if valid_game:
			print('   Valid game!')
			id_sum += int(game[0])

	return id_sum


total = main()
print(f'ID sum: {total}')
