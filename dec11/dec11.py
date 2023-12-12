from input_handler import convert_input


def parse_map(data):
	galaxies = []
	empty_rows = [i for i in range(len(data))]
	empty_columns = [j for j in range(len(data[0]))]

	for r in range(len(data)):
		row_set = set(data[r])
		if '#' in row_set:
			if r in empty_rows:
				empty_rows.remove(r)
		for c in range(len(data[0])):
			if data[r][c] == '#':
				position = (r, c)
				# print(f'Galaxy found at {position}')
				galaxies.append(position)
				if c in empty_columns:
					empty_columns.remove(c)

	return galaxies, empty_rows, empty_columns


def find_distance(galaxy, next_galaxy, empty_rows, empty_columns):
	gal_row = galaxy[0]
	gal_col = galaxy[1]
	ng_row = next_galaxy[0]
	ng_col = next_galaxy[1]

	empty_col_count = 0
	empty_row_count = 0

	print(f'Galaxy 1: {galaxy}, galaxy 2: {next_galaxy}')

	row_diff = abs(gal_row - ng_row)
	print(f'   Row diff: {row_diff}')
	print(f'   Row range to check: {(gal_row, ng_row)}')
	for er in empty_rows:
		if er in range(min(gal_row, ng_row), max(gal_row, ng_row)):
			print(f'      Path crosses empty row {er}')
			empty_row_count += 1

	col_diff = abs(gal_col - ng_col)
	print(f'   Col diff: {col_diff}')
	print(f'   Col range to check: {(gal_col, ng_col)}')
	for ec in empty_columns:
		if ec in range(min(gal_col, ng_col), max(gal_col, ng_col)):
			print(f'      Path crosses empty col {ec}')
			empty_col_count += 1

	steps = row_diff + col_diff
	print(f'   Initial step count: {steps}')
	extra_rc = (empty_row_count + empty_col_count) * 999999
	print(f'   Extra count: ({empty_row_count} + {empty_col_count}) = {extra_rc}')
	steps += extra_rc

	return steps


def main():
	with open('input.txt') as i:
		i_raw = i.readlines()

	data = convert_input(i_raw)

	total_sum = 0

	# for line in data:
	# 	print(line)

	galaxies, empty_rows, empty_columns = parse_map(data)

	print(f'{len(galaxies)} galaxies: {galaxies}')
	print(f'{len(empty_rows)} empty rows: {empty_rows}')
	print(f'{len(empty_columns)} empty columns: {empty_columns}')

	pair_count = 0

	for g in range(len(galaxies)):
		for ng in range(g + 1, len(galaxies)):
			steps = find_distance(galaxies[g], galaxies[ng], empty_rows, empty_columns)
			total_sum += steps
			pair_count += 1
			print(f'      {steps} steps between galaxy {galaxies[g]} and galaxy {galaxies[ng]}')

	print(f'{pair_count} pairs of galaxies counted')
	# for each galaxy, find h/w diff between each other galaxy

	return total_sum


total = main()
print(f'Total: {total}')
