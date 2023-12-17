def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_list = []
    for line in data_strip:
        data_list = line.split(',')

    return data_list
