def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    new_data = []
    for line in data_strip:
        new_data.append(line.split(' '))
    # print(new_data)
    for n in range(len(new_data)):
        new_data[n] = [int(x) for x in new_data[n]]

    return new_data
