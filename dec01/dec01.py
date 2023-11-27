from input_handler import convert_input

with open('input.txt') as i:
	i_raw = i.readlines()

data = convert_input(i_raw)
print(data)
