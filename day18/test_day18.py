#!/usr/bin/env python3
# import pytest
from day18 import solve1, part1, solve2, part2


def test_solve1():
    assert solve1("2 + 3 * 6") == 30
    assert solve1("1 + (2 * 3)") == 7


def test_part1_small():
    assert part1("small.txt") == 463


def test_part1_input():
    assert part1("input.txt") == 14208061823964


def test_solve2():
    assert solve2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert solve2("2 * 3 + (4 * 5)") == 46
    assert solve2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert solve2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert solve2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def test_part2_input():
    assert part2("input.txt") == 320536571743074
