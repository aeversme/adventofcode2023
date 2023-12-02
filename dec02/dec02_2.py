from input_handler import convert_input


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	power_sum = 0

	for game in data:
		power = 1
		dice = {
			'red': 0,
			'green': 0,
			'blue': 0
		}
		print(game)
		for subset in game[1]:
			print(f'   Subset: {subset}')
			for color in subset:
				print(f'      Color: {color}')
				if int(color[0]) > dice[color[1]]:
					dice[color[1]] = int(color[0])
			print(f'      Dice: {dice}')

		for _, value in dice.items():
			power *= value
		print(f'   Total game power: {power}')

		power_sum += power

	return power_sum


total = main()
print(f'ID sum: {total}')
