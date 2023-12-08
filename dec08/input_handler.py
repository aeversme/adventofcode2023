def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    lr = data_strip.pop(0)
    camel_map = {}

    for i in range(len(data_strip)):
        if data_strip[i]:
            temp = data_strip[i].split('=')
            mk = temp[0].strip(' ')
            temp[1] = temp[1].strip(' ')
            mv = [temp[1][1:4], temp[1][6:9]]
            camel_map[mk] = mv

    return lr, camel_map
