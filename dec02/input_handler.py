def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [j.split(':') for j in data_strip]
    for k in data_split:
        k[1] = k[1].split(';')
    for line in data_split:
        # print(f'line: {line[1]}')
        # print(f'   item: {line[1]}')
        for n in range(len(line[1])):
            line[1][n] = line[1][n].split(',')
            # print(line[1][n])
            for q in range(len(line[1][n])):
                line[1][n][q] = line[1][n][q].strip(' ').split(' ')
        line[0] = line[0][5:]

    return data_split
