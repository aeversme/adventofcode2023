from input_handler import convert_input


def seeds_to_ranges(seeds):
	seed_ranges = []
	for i in range(len(seeds)):
		if i % 2 == 0:
			start = seeds[i]
			end = start + (seeds[i + 1] - 1)
			seed_ranges.append([start, end])

	return seed_ranges


def convert_number(almanac, process, number):
	new_number = 0
	for k, v in almanac[process].items():
		if v['source_start'] <= number <= v['source_end']:
			return number + v['modifier']
	if new_number == 0:
		return number


def reverse_convert(almanac, process, number):
	new_number = 0
	for k, v in almanac[process].items():
		if v['destination_start'] <= number <= v['destination_end']:
			return number - v['modifier']
	if new_number == 0:
		return number
	return


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	seeds, almanac = convert_input(i_raw)
	seed_ranges = seeds_to_ranges(seeds)
	print(seeds)
	print(seed_ranges)

	processes = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
				 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']

	reverse_processes = ['humidity-to-location map:', 'temperature-to-humidity map:', 'light-to-temperature map:',
						 'water-to-light map:', 'fertilizer-to-water map:', 'soil-to-fertilizer map:',
						 'seed-to-soil map:']

	for k, v in almanac.items():
		print(f'{k}')
		for p, q in v.items():
			print(f'   {p}: {q}')

	lowest = 1000000000000000

	location = 0
	seed_found = False

	mask = 2**20 - 1

	for loc in range(100000000, 1000000000):
		if loc & mask == 0:
			print(loc)

		location = loc
		for i in range(len(reverse_processes)):
			# print(f'{loc} going into {reverse_processes[i]}')
			loc = reverse_convert(almanac, reverse_processes[i], loc)
			# print(f'   Result: {loc}')

		# print('\n')

		for r in range(len(seed_ranges)):
			if seed_ranges[r][0] <= loc <= seed_ranges[r][1]:
				print(f'Seed {loc} found in seed range!')
				print(f'Corresponding location: {location}')
				seed_found = True
				break
			# else:
				# print(f'Seed {loc} not found in seed range: {seed_ranges[r]}.')

		if seed_found:
			break

	# for num in seeds:
	# 	for i in range(len(processes)):
	# 		print(f'{num} going into {processes[i]}')
	# 		num = convert_number(almanac, processes[i], num)
	# 		print(f'   Result: {num}')
	# 	print('\n')
	# 	if num < lowest:
	# 		lowest = num

	return lowest


low = main()
# print(f'Lowest: {low}')
