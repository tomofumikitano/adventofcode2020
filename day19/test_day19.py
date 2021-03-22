#!/usr/bin/env python3
# import pytest
from day19 import part1, part2


def test_part1_small():
    assert part1("./small.txt") == 2


def test_part1_input():
    assert part1("./input.txt") == 192


def test_part2_small():
    assert part2("./small_part2.txt") == 12


def test_part2_input():
    assert part2("./input.txt") == 296
