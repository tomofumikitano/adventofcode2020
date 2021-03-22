#!/usr/bin/env python3

MODULO = 20201227


def find_loop(pubkey, subject=7):
    loop = 1
    value = 1
    while True:
        value = (value * subject) % MODULO
        if value == pubkey:
            return loop
        loop += 1


def find_enckey(pubkey, loop):
    result = 1
    for i in range(loop):
        result = (result * pubkey) % MODULO
    return result


def part1(pubkey_card, pubkey_door):
    loop_card = find_loop(pubkey_card)
    loop_door = find_loop(pubkey_door)

    print("loop_card:", loop_card)
    print("loop_door:", loop_door)

    if loop_card < loop_door:
        enckey = find_enckey(pubkey_door, loop_card)
    else:
        enckey = find_enckey(pubkey_card, loop_door)

    return enckey


if __name__ == "__main__":
    # print(part1(5764801, 17807724))
    print(part1(15113849, 4206373))
