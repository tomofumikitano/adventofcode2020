#!/usr/bin/env python3
import pytest
from day22 import part1, part2


def test_part1_small():
    assert part1("small.txt") == 306


def test_part1_input():
    assert part1("input.txt") == 32272


def test_part2_small():
    assert part2("small.txt") == 291


def test_part2_input():
    assert part2("input.txt") == 33206
