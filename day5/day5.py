#!/usr/bin/env python3

def find_row(seat_str: str):
    return int(seat_str[:7].translate(str.maketrans('FB', '01')), 2)

def find_col(seat_str: str):
    return int(seat_str[7:].translate(str.maketrans('LR', '01')), 2)

# def find_row(seat_str: str):
#     lo = 0
#     hi = 127
#     for x in seat_str[:7]:
#         if x == 'F':
#             hi = hi - (hi - lo) // 2 - 1
#         else:  # x == 'B':
#             lo = lo + (hi - lo) // 2 + 1
#     assert hi == lo
#     return lo


# def find_col(seat_str: str):
#     lo = 0
#     hi = 7
#     for x in seat_str[-3:]:
#         if x == 'L':
#             hi = hi - (hi - lo) // 2 - 1
#         else:  # x == 'R':
#             lo = lo + (hi - lo) // 2 + 1
#     assert hi == lo
#     return lo


def find_seat_id(seat_str):
    return find_row(seat_str) * 8 + find_col(seat_str)


def part1(_input="input.txt"):
    return max([find_seat_id(line.strip()) for line in open(_input)])


def part2(_input="input.txt"):
    seats = {}
    with open(_input) as f:
        for line in f:
            line = line.strip()
            seats[find_seat_id(line)] = line

    for i in range(part1(_input)):
        if i not in seats.keys():
            print(f"{i} is missing")


if __name__ == "__main__":
    # find_row('FBFBBFFRLR')
    # find_col('FBFBBFFRLR')

    assert find_seat_id('BFFFBBFRRR') == 567
    assert find_seat_id('FFFBBBFRRR') == 119
    assert find_seat_id('BBFFBBFRLL') == 820

    print("Part 1:", part1("input.txt"))
    # print("Part 2:", part2("input.txt"))
