#!/usr/bin/env python3
import pytest
from day import part1, part2


def test_part1_small():
    assert part1("small.txt") == None


@pytest.mark.skip
def test_part1_input():
    assert part1("input.txt") == None


@pytest.mark.skip
def test_part2_small():
    assert part2("small.txt") == None


@pytest.mark.skip
def test_part2_input():
    assert part2("input.txt") == None
