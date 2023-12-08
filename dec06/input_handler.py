def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [i.split(' ') for i in data_strip]
    new_data = []
    for line in data_split:
        new_line = []
        for i in line:
            if i:
                new_line.append(i)
        new_data.append(new_line)

    return new_data
