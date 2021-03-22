#!/usr/bin/env python3
from itertools import product
from collections import defaultdict


def build_neibours_delta(dim=3):
    origin = tuple(0 for _ in range(dim))
    return [p for p in product(*[[-1, 0, 1] for _ in range(dim)]) if p != origin]


NEIBOURS_3D = build_neibours_delta(dim=3)
NEIBOURS_4D = build_neibours_delta(dim=4)


def load_input(input_file, dim=3):
    key = [0 for _ in range(dim)]
    cubes = defaultdict(lambda: '.')
    x = 0
    with open(input_file) as f:
        for line in f:
            key[0] = x
            for y, state in enumerate(line.rstrip()):
                key[1] = y
                cubes[tuple(key)] = state
            x += 1
    return cubes


def print_cubes_3d(cubes):
    x_axis = sorted({k[0] for k in cubes})
    y_axis = sorted({k[1] for k in cubes})
    z_axis = sorted({k[2] for k in cubes})
    print(f"{len(x_axis)}x{len(y_axis)}x{len(z_axis)}\n")
    for z in sorted(z_axis):
        print(f"z={z}")
        for x in x_axis:
            print(''.join([cubes[(x, y, z)] for y in y_axis]))
        print()


def print_cubes_4d(cubes):
    x_axis = sorted({k[0] for k in cubes})
    y_axis = sorted({k[1] for k in cubes})
    z_axis = sorted({k[2] for k in cubes})
    w_axis = sorted({k[3] for k in cubes})
    print(f"{len(x_axis)}x{len(y_axis)}x{len(z_axis)}x{len(w_axis)}\n")
    raise NotImplementedError("Not supported")


def count_active_neibours_3d(cubes, cood):
    count = 0
    for delta in NEIBOURS_3D:
        key_neibour = tuple(c + d for c, d in zip(cood, delta))
        if cubes[key_neibour] == '#':
            count += 1
    return count


def count_active_neibours_4d(cubes, p):
    count = 0
    for (dx, dy, dz, dw) in NEIBOURS_4D:
        if (p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw) in cubes:
            if cubes[(p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw)] == '#':
                count += 1
    return count


def next_state(cubes, p, count_active_neibours=count_active_neibours_3d):
    if cubes[p] == '#':
        if count_active_neibours(cubes, p) in {2, 3}:
            return '#'
        return '.'
    elif cubes[p] == '.':
        if count_active_neibours(cubes, p) == 3:
            return '#'
        return '.'
    else:
        raise Exception("Unexpected path")


def new_positions_3d(cubes):
    x_axis = {k[0] for k in cubes}
    y_axis = {k[1] for k in cubes}
    z_axis = {k[2] for k in cubes}
    x_axis |= {min(x_axis)-1, max(x_axis)+1}
    y_axis |= {min(y_axis)-1, max(y_axis)+1}
    z_axis |= {min(z_axis)-1, max(z_axis)+1}
    return product(x_axis, y_axis, z_axis)


def new_positions_4d(cubes):
    x_axis = {k[0] for k in cubes}
    y_axis = {k[1] for k in cubes}
    z_axis = {k[2] for k in cubes}
    w_axis = {k[3] for k in cubes}
    x_axis |= {min(x_axis)-1, max(x_axis)+1}
    y_axis |= {min(y_axis)-1, max(y_axis)+1}
    z_axis |= {min(z_axis)-1, max(z_axis)+1}
    w_axis |= {min(w_axis)-1, max(w_axis)+1}
    return product(x_axis, y_axis, z_axis, w_axis)


def part1(input_file):
    cubes = load_input(input_file)
    # print_cubes(cubes)
    for cycle in range(1, 7):
        points = new_positions_3d(cubes)
        changes = {}

        for p in points:
            changes[p] = next_state(cubes, p)

        for k, v in changes.items():
            cubes[k] = v

        # print(f"After {cycle} cycle:\n")
        # print_cubes(cubes)
        # input("\nPress any key to continue... ")
    return sum(v == '#' for v in cubes.values())


def part2(input_file):
    cubes = load_input(input_file, dim=4)
    # print_cubes_4d(cubes)
    # input()
    for cycle in range(1, 7):
        points = new_positions_4d(cubes)
        changes = {}

        for p in points:
            changes[p] = next_state(
                cubes, p, count_active_neibours=count_active_neibours_4d)

        for k, v in changes.items():
            cubes[k] = v

        # print(f"After {cycle} cycle:\n")
        # print_cubes(cubes)
        # input("\nPress any key to continue... ")
    return sum(v == '#' for v in cubes.values())


if __name__ == "__main__":
    print(part1("input"))
    print(part2("input"))
