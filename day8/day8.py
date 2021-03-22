#!/usr/bin/env python3
from copy import deepcopy


def run(intcodes):
    ip, acc = 0, 0
    visited = set()
    while ip not in visited and ip < len(intcodes):
        visited.add(ip)
        operation, argument = intcodes[ip]

        if operation == "acc":
            acc += argument

        if operation == "jmp":
            ip += argument
        elif operation in {"nop", "acc"}:
            ip += 1

    return (acc, ip)


def part2(intcodes):

    SWAP_TABLE = {"nop": "jmp", "jmp": "nop"}

    def copy_flipped(intcodes, i):
        copy = deepcopy(intcodes)
        copy[i][0] = SWAP_TABLE[copy[i][0]]
        return copy

    ip_to_flip = [i for (i, op) in enumerate(
        intcodes) if op[0] in {"jmp", "nop"}]

    for i in ip_to_flip:
        intcodes_copy = copy_flipped(intcodes, i)
        result = run(intcodes_copy)
        if result[1] >= len(intcodes):
            return result


if __name__ == "__main__":

    intcodes = []
    for line in open("input.txt"):
        op, arg = line.strip().split()
        intcodes.append([op, int(arg)])

    print("Part 1:", run(intcodes))
    print("Part 2:", part2(intcodes))
