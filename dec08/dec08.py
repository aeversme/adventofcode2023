from input_handler import convert_input
import math


def get_factors(number):
    n = int(number ** .5) + 1
    x = number
    divisors = []
    era = [1] * n
    primes = []
    for p in range(2, n):
        if era[p]:
            primes.append(p)
            while x % p == 0:
                x //= p
                divisors.append(p)
            for i in range(p * p, n, p):
                era[i] = False
    if x != 1:
        divisors.append(x)
    return divisors


def next_node(current_node, direction, camel_map):
    pair = camel_map[current_node]
    # print(f'   Pair: {pair}, direction: {direction}')
    if direction == 'L':
        new_node = pair[0]
    else:
        new_node = pair[1]
    # print(f'      Next step: {new_node}')
    return new_node


def traverse_map(node, directions, camel_map):
    steps = 0
    index = 0

    while True:
        if node[-1] == 'Z':
            return steps

        direction = directions[index]
        if index == len(directions) - 1:
            index = 0
        else:
            index += 1

        # print(f'Finding steps for {node}')
        node = next_node(node, direction, camel_map)
        steps += 1


# return steps


def main():
    with open('input.txt') as i:
        i_raw = i.readlines()

    directions, camel_map = convert_input(i_raw)
    # print(camel_map)

    total_sum = 0

    # part 1
    total_sum = traverse_map('AAA', directions, camel_map)

    # part 2
    all_divisors = []
    node_list = []
    for node_key in camel_map.keys():
        if node_key[-1] == 'A':
            node_list.append(node_key)
    print(f'Starting node list: {node_list}\n')

    for node in node_list:
        steps_for_node = traverse_map(node, directions, camel_map)
        divisors = get_factors(steps_for_node)
        all_divisors.append(divisors)
        print(f'{node}: {steps_for_node}, divisors: {divisors}')

    num = math.lcm(all_divisors[0][0], all_divisors[1][0], all_divisors[2][0],
                   all_divisors[3][0], all_divisors[4][0], all_divisors[5][0])
    print(num)
    print(num * all_divisors[0][1])

    return total_sum


total = main()
print(f'Total: {total}')
