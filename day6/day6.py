#!/usr/bin/env python3

DEFAULT_INPUT = "./input_small.txt"


def read_blocks(input_file):
    return open(input_file).read().split("\n\n")


def part1(groups: list):
    return sum(len(set.union(*[set(x) for x in g.split()])) for g in groups)


def part2(groups: list):
    return sum(len(set.intersection(*[set(x) for x in g.split()])) for g in groups)


if __name__ == "__main__":

    groups_small = read_blocks("./input_small.txt")
    groups = read_blocks("./input6.txt")

    assert part1(groups_small) == 11
    assert part1(groups) == 6170

    assert part2(groups_small) == 6
    assert part2(groups) == 2947
