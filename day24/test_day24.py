#!/usr/bin/env python3
import pytest
from day24 import part1, part2


def test_part1_small():
    assert part1("small.txt") == 10


def test_part1_input():
    assert part1("input.txt") == 326


def test_part2_small():
    assert part2("small.txt") == 2208


def test_part2_input():
    assert part2("input.txt") == 3979
