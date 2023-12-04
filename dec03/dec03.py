from input_handler import convert_input


def find_number(line, index):
    num = ''
    line = line[index:]
    new_index = index
    for i in range(len(line)):
        if line[i].isdigit():
            num += line[i]
            new_index += 1
        else:
            break
    return num, new_index


def create_number_list(data):
    numbers_list = []
    line_number = 0
    for line in data:
        print(line)
        index = 0
        for i in range(len(line)):
            if index >= (len(line) - 1):
                break
            elif line[index].isdigit():
                start_index = index
                current_number, index = find_number(line, index)
                end_index = start_index + (len(current_number) - 1)
                if len(current_number) == 3:
                    middle_num = int(start_index) + 1
                    index_range = [start_index, middle_num, end_index]
                else:
                    index_range = [start_index, end_index]
                print(f'   Number found: {current_number}, start: {start_index}, '
                      f'end: {end_index}, line: {line_number}, range: {index_range}')
                numbers_list.append([current_number, start_index, end_index, line_number, index_range])
            else:
                index += 1
        line_number += 1

    return numbers_list


def line_col_range(total_lines, line_length, line_number, start, end):
    if line_number == 0:
        line_range = [0, 1]
    elif line_number == (total_lines - 1):
        line_range = [-1, 0]
    else:
        line_range = [-1, 1]

    start = int(start)
    end = int(end)

    if start == 0 and end != (line_length - 1):
        col_range = [0, end + 1]
    elif end == (line_length - 1):
        col_range = [start - 1, end]
    else:
        col_range = [start - 1, end + 1]

    return line_range, col_range


def check_number_for_symbol(data, number, num_sum):
    num = number[0]
    start = number[1]
    end = number[2]
    line_number = number[3]
    total_lines = len(data)
    line_length = len(data[line_number])
    line_range, col_range = line_col_range(total_lines, line_length, line_number, start, end)
    print(f'Number: {num}')
    print(f'   Line range: {line_range}, col range: {col_range}')
    print(f'   Current sum: {num_sum}')

    symbol_found = False

    for li in range(line_range[0], line_range[1] + 1):
        for ci in range(col_range[0], col_range[1] + 1):
            char = data[line_number + li][ci]
            # print(char)
            if not char.isdigit() and char != '.':
                num_sum += int(num)
                print(f'   Symbol found! New sum: {num_sum}\n')
                symbol_found = True
                break
        if symbol_found:
            break

    if not symbol_found:
        print('   No symbol found.')

    return num_sum


def check_around_star(numbers_list, star_line, line_range, col_range, g_total, num_gears):
    nums_found = 0
    temp_product = 1
    for li in range(line_range[0], line_range[1] + 1):
        for number in numbers_list:
            # [current_number, start_index, end_index, line_number, index_range]
            if number[3] == star_line + li:
                print(f'      Number in line range: {number}')
                for ci in range(col_range[0], col_range[1] + 1):
                    if ci in number[4]:
                        print(f'         Number {number[0]} adjacent to *! (line {number[3]}, range {number[4]})')
                        nums_found += 1
                        temp_product *= int(number[0])
                        print(f'            New temp product: {temp_product}')
                        break

    if nums_found > 1:
        g_total += temp_product
        num_gears += 1
        print(f'   ***Temp product {temp_product} added to g_total.')

    return g_total, num_gears


def main():
    with open('input.txt') as d:
        data_raw = d.readlines()

    data = convert_input(data_raw)

    # create number data structure
    numbers_list = create_number_list(data)
    print(f'\nThere are {len(numbers_list)} numbers in the input.\n')

    # part 1
    num_sum = 0
    # for number in numbers_list:
    #     num_sum = check_number_for_symbol(data, number, num_sum)

    # part 2
    g_total = 0
    line_number = 0
    total_lines = len(data)
    num_stars = 0
    num_gears = 0
    for line in data:
        line_length = len(line)
        for i in range(len(line)):
            if line[i] == '*':
                star_line = line_number
                star_col = i
                print(f'* found; line: {star_line}, col: {star_col}')
                num_stars += 1
                line_range, col_range = line_col_range(total_lines, line_length, line_number, star_col, star_col)
                print(f'   Line range: {line_range}, col range: {col_range}')

                g_total, num_gears = check_around_star(numbers_list, star_line, line_range, col_range, g_total, num_gears)
        line_number += 1

    return num_sum, g_total, num_stars, num_gears


total, gear_total, stars, gears = main()
print(f'\nTotal: {total}, gear total: {gear_total}, stars: {stars}, gears: {gears}')
