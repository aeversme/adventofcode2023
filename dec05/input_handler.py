def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    seeds = data_strip.pop(0)
    seeds_split = seeds.split(' ')
    seeds_split.pop(0)
    seeds_int = [int(x) for x in seeds_split]

    almanac = {}

    index = 0
    key = ''
    for i in range(len(data_strip)):
        item = data_strip[i]
        index += 1
        if item == '':
            continue
        if item[0].isalpha():
            key = item
            almanac[item] = {}
            index = 0
        else:
            item_list = item.split(' ')
            start = int(item_list[1])
            end = int(item_list[1]) + (int(item_list[2]) - 1)
            modifier = int(item_list[0]) - int(item_list[1])
            almanac[key][index] = {
                'source_start': start,
                'source_end': end,
                'destination_start': start + modifier,
                'destination_end': end + modifier,
                'modifier': modifier
            }

    return seeds_int, almanac
