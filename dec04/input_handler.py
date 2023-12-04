def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [j.split(':') for j in data_strip]
    for k in data_split:
        k[1] = k[1].split('|')
    for line in data_split:
        # print(f'line: {line[1]}')
        # print(f'   item: {line[1]}')
        for n in range(len(line[1])):
            line[1][n] = line[1][n].strip(' ').split(' ')
            # print(line[1][n])
            new_list = []
            for q in range(len(line[1][n])):
                try:
                    new_list.append(int(line[1][n][q]))
                except ValueError:
                    continue
            line[1][n] = new_list
        line[0] = int(line[0][5:])

    return data_split
