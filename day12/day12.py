#!/usr/bin/env python3

EAST_ = 0
SOUTH = 1
WEST_ = 2
NORTH = 3

instructions = []

with open('input.txt') as f:
    for line in f:
        action, value = line[0], int(line[1:])
        instructions.append((action, value))

facing = EAST_
x_ship, y_ship = 0, 0

tbl = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

for a, v in instructions:
    if a in tbl:
        x_ship, y_ship = x_ship + v * tbl[a][0], y_ship + v * tbl[a][1]
    elif a == 'F':
        if facing == EAST_:
            x_ship = x_ship + v
        if facing == WEST_:
            x_ship = x_ship - v
        if facing == NORTH:
            y_ship = y_ship + v
        if facing == SOUTH:
            y_ship = y_ship - v
    elif a == 'R':
        facing = (facing + v / 90) % 4
    elif a == 'L':
        facing = (facing - v / 90) % 4
    # print((a, v), (x_ship, y_ship), facing)

print("Part 1:", abs(x_ship) + abs(y_ship))


# part 2
def rotate_right(x, y, i):
    return {
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x)
    }[i]


def rotate_left(x, y, i):
    return {
        90: (-y, x),
        180: (-x, -y),
        270: (y, -x)
    }[i]


(x_ship, y_ship) = (0, 0)
(x_wayp, y_wayp) = (10, 1)
for a, v in instructions:
    if a in tbl:
        x_wayp, y_wayp = x_wayp + v * tbl[a][0], y_wayp + v * tbl[a][1]
    elif a == 'F':
        x_ship, y_ship = x_ship + v * x_wayp, y_ship + v * y_wayp
    elif a == 'R':
        x_wayp, y_wayp = rotate_right(x_wayp, y_wayp, v)
    elif a == 'L':
        x_wayp, y_wayp = rotate_left(x_wayp, y_wayp, v)
    # print(f"{a}{int(v):3}", (x_ship, y_ship), (x_wayp, y_wayp))

print("Part 2:", abs(x_ship) + abs(y_ship))
