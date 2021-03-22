#!/usr/bin/env python3
# from collections import deque
from collections import defaultdict


def solve(data: str, target: int):

    data = [int(c) for c in data.split(",")]

    mem = defaultdict(list)
    last = None

    turn = 0
    for x in data:
        mem[x].append(turn)
        turn += 1

    print(turn, mem)
    # input()

    last = data[-1]
    while turn < target:

        if len(mem[last]) == 2:
            v = mem[last][0] - mem[last][1]
            mem[v].append(turn)
        else:
            v = 0
            mem[v].append(turn)

        mem[v][1] = mem[v][0]
        mem[v][0] = turn

        last = v

        turn += 1

    return last


if __name__ == "__main__":
    print(solve("0,3,6", 2020))
    # print(solve("9,12,1,4,17,0,18", 30000000))
