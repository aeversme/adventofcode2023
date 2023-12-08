from input_handler import convert_input


def process_race(race):
	time = race[0]
	record = race[1]
	winning_count = 0

	for m in range(time):
		speed = m
		distance = speed * (time - m)
		# print(f'   {m}; speed: {speed}, distance: {distance}')
		# print(f'   Record: {record}')
		if distance > record:
			# print(f'      Winning race!')
			winning_count += 1

	return winning_count


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	races = []

	# part 1
	# for i in range(1):
	# 	for j in range(1, len(data[i])):
	# 		new_race = [int(data[i][j]), int(data[i + 1][j])]
	# 		races.append(new_race)

	# part 2
	races = [[int(data[0][1] + data[0][2] + data[0][3] + data[0][4]), int(data[1][1] + data[1][2] + data[1][3] + data[1][4])]]

	number = 1

	for race in races:
		print(race)
		winning_count = process_race(race)
		print(f'Winning count: {winning_count}')
		number *= winning_count

	return number


total = main()
print(f'Total: {total}')
