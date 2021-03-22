#!/usr/bin/env python3
from collections import defaultdict


_input = "9,12,1,4,17,0,18"
data = [ int(x) for x in _input.split(",")]

target = 30000000 
turn = 1
mem = defaultdict(list)

for x in data:
    mem[x].append(turn)
    turn += 1

last = data[-1]
while turn <= target:
    c = len(mem[last])

    if c == 1:
        mem[0].append(turn)
        last = 0
    else:
        n = mem[last][-1] - mem[last][-2]
        mem[n].append(turn)
        last = n
    turn += 1

print(last)
