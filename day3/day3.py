#!/usr/bin/env python3
import math

def is_tree(grid, r, c):
    result = '.'
    if grid[r][c] == '#':
        result = '#'
    # print(f"_map[{r}][{c}] = {result}")
    return result == '#'


def count_trees(input="input.txt", slope=(3, 1)):
    num_trees = 0

    grid = [line.strip() for line in open(input)]
    rows = len(grid)
    cols = len(grid[0])
    # print(f"rows = {rows}, cols = {cols}")

    row, col = 0, 0
    while row < rows - 1:
        col = (col + slope[0]) % cols
        row += slope[1]
        if is_tree(grid, row, col):
            num_trees += 1

    return num_trees


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [count_trees(slope=s) for s in slopes]
    # print(trees)
    return math.prod(trees)


if __name__ == "__main__":
    print(count_trees(slope=(3, 1)))
    print(part2())
    print("🏂")
    print("🌲")
