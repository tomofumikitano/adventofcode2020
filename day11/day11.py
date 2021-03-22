#!/usr/bin/env python3
from itertools import product


def build_grid(filename):
    grid = list()
    with open(filename) as f:
        for line in f:
            grid.append([c for c in line.strip()])
    return grid


def print_grid(grid):
    for line in grid:
        print(''.join(line))


def count_occupied_total(grid):
    return sum(line.count('#') for line in grid)


def count_seats(grid):
    return sum(line.count('#') + line.count('L') for line in grid)


def occupied_adjacent(grid, i, j, cache=None):
    return sum(grid[y][x] == '#' for (y, x) in neighbours(grid, i, j, cache))


DIRECTIONS = {
    (-1, -1), (-1, 0), (-1, +1),
    (0, -1),          (0, +1),
    (+1, -1), (+1, 0), (+1, +1)
}


def neighbours(grid, i, j, cache):
    if cache is not None and (i, j) in cache:
        return cache[(i, j)]

    height, width = len(grid), len(grid[0])

    result = []
    for v in DIRECTIONS:
        x, y = i + v[0], j + v[1]
        if x in range(0, height) and y in range(0, width):
            result.append((x, y))

    if cache is not None:
        cache[(i, j)] = result
    return result


def visible_seats(grid, i, j, cache=None):
    """
    Returns: 
        list of list of visible seats for 8 directions
    """
    if cache is not None and (i, j) in cache:
        return cache[(i, j)]

    result = []
    height, width = len(grid), len(grid[0])
    for v in DIRECTIONS:
        seats_in_v = []
        for n in range(1, max(height, width)):
            x, y = i + n * v[0], j + n * v[1]
            if x in range(0, height) and y in range(0, width):
                seats_in_v.append((x, y))
        result.append(seats_in_v)

    if cache is not None:
        cache[(i, j)] = result
    return result


def count_occupied_visible(grid, i, j, cache=None):
    result = 0

    for direction in visible_seats(grid, i, j, cache):
        for (x, y) in direction:
            if grid[x][y] == '#':
                result += 1
                break
            if grid[x][y] == 'L':
                break

    return result


def simulate(grid, count_occupied=occupied_adjacent, threshold=4, cache=None):
    flips = set()

    for (i, j) in product(range(len(grid)), range(len(grid[0]))):
        if grid[i][j] == 'L' and count_occupied(grid, i, j, cache) == 0:
            flips.add((i, j))
        if grid[i][j] == '#' and count_occupied(grid, i, j, cache) >= threshold:
            flips.add((i, j))

    for (i, j) in flips:
        if grid[i][j] == '#':
            grid[i][j] = 'L'
        else:
            grid[i][j] = '#'
    return grid


# class Cache():
#
#     _cache = None
#     miss = 0
#     hit = 0
#
#     def __init__(self):
#         self._cache = dict()
#
#     def __contains__(self, k):
#         if k in self._cache:
#             self.hit += 1
#             return True
#         else:
#             self.miss += 1
#             return False
#
#     def __getitem__(self, k):
#         return self._cache[k]
#
#     def __setitem__(self, k, v):
#         self._cache[k] = v
#
#     def __str__(self):
#         return f"Cache size: {len(self._cache)}, hit: {self.hit}, miss: {self.miss}"


def solve(grid, count_rule=occupied_adjacent, threshold=4):
    prev_count = None
    cache = dict()
    while True:
        grid = simulate(grid, count_rule, threshold, cache=cache)
        count = count_occupied_total(grid)
        if count == prev_count:
            return count
        prev_count = count


if __name__ == "__main__":

    import cProfile
    cProfile.run(
        'print(solve(build_grid("input.txt"), count_rule=count_occupied_visible, threshold=5))')

    # grid = build_grid("input.txt")
    # print(solve(grid, count_occupied_visible, threshold=5))
