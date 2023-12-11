def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    data_strip = ['.' * len(data_strip[0])] + data_strip + ['.' * len(data_strip[0])]
    for i in range(len(data_strip)):
        data_strip[i] = '.' + data_strip[i] + '.'

    return data_strip
