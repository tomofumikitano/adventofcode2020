#!/usr/bin/env python3

def mask_value(value, mask):
    m1 = int(mask.replace("X", "0"), 2)
    m2 = int(mask.replace("X", "1"), 2)
    return (int(value) | m1) & m2


def part1(filename):
    mem = dict()
    mask = None
    with open(filename) as f:
        for line in f:
            key, value = line.strip().split(" = ")
            if key == "mask":
                mask = value
            elif key[0:3] == "mem":
                address = int(key.replace("mem[", "").replace("]", ""))
                value = mask_value(value, mask)
                mem[address] = value
    return sum(mem.values())


# def build_mask_list(mask):
#     result = [mask]
#     idx = [i for i, c in enumerate(mask) if c == 'X']
#     for i in idx:
#         tmp = []
#         for s in result:
#             tmp.append(s[:i] + '0' + s[i+1:])
#             tmp.append(s[:i] + '1' + s[i+1:])
#         result = tmp
#     from itertools import product
#     for x in product(idx, {'0', '1'}):
#         print(x)
#     return result

def generate_masks(index):
    """
    Args: 
        index: list of indices where 'X' appear
    Returns:
    """

    if len(index) == 1:
        return [0, 1]

    result = []
    index = sorted(index, reverse=True)
    p = index[0]
    for sub_mask in generate_masks(index[1:]):
        a0 = (0 << p) ^ sub_mask
        a1 = (1 << p) ^ sub_mask
        # print("Appending", a0, a1)
        result.append(a0)
        result.append(a1)

    return result


# index = [ i for i, c in enumerate("0X1001X") if c == 'X' ]
# print(index)
# print(generate_masks(index))

def generate_actual_memory_addresses(address, mask):
    __import__('ipdb').set_trace()
    print(int(mask.replace("X", "0"), 2))
    base_address = address | int(mask.replace("X", "0"), 2)
    print("base address:", base_address)
    index_X = [len(mask) - i - 1 for i, c in enumerate(mask) if c == 'X']
    print("Index:", index_X)

    result = [base_address + m for m in generate_masks(index_X)]
    print("Returning", result)
    return result

    # address_padded = bin(address)[2:].zfill(len(mask)) # Remove leading '0b'
    # result = ""
    # for a, m in zip(address_padded, mask):
    #     if m == '0':
    #         result += a
    #     else:
    #         result += m

    # def build_mask_list(mask):
    #     template = mask.replace("X", "{}")
    #     count_X = str.count(mask, "X")
    #     for i in range(2 ** count_X):
    #         i_bin = bin(i).replace('0b', '')
    #         padding = '0' * (count_X - len(i_bin))
    #         yield template.format(*list(padding + i_bin))
    #
    # return build_mask_list(result)



def part2(filename):
    mem = dict()
    with open(filename) as f:
        for line in f:
            key, value = line.strip().split(" = ")
            if key == "mask":
                mask = value
            elif key[0:3] == "mem":
                address = int(key.replace("mem[", "").replace("]", ""))
                for a in generate_actual_memory_addresses(address, mask):
                    # a = int(a, 2)
                    mem[a] = int(value)
    return sum(mem.values())


if __name__ == "__main__":
    mask = "000000000000000000000000000000X1001X"
    address = 42
    print(list(generate_actual_memory_addresses(address, mask)))

    # filename = "./qh9d5y"
    # print("Part 1:", part1(filename))
    # print("Part 2:", part2(filename))
    pass
