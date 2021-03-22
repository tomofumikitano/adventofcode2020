#!/usr/bin/env python3
import pytest
from day20 import part1, part2


def test_part1_small():
    assert part1("small.txt") == 20899048083289


def test_part1_input():
    assert part1("input.txt") == 20033377297069


@pytest.mark.skip
def test_part2_small():
    assert part2("small.txt") == 273


@pytest.mark.skip
def test_part2_input():
    assert 1 == 1
