def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_split = [j.split(' ') for j in data_strip]

    for k in data_split:
        k[1] = int(k[1])

    return data_split
