#!/usr/bin/env python3
import pytest
from day15 import solve


def test_part1_small():
    assert solve("1,3,2", 2020) == 1
    assert solve("2,1,3", 2020) == 10
    assert solve("1,2,3", 2020) == 27
    assert solve("2,3,1", 2020) == 78
    assert solve("3,2,1", 2020) == 438
    assert solve("3,1,2", 2020) == 1836


def test_part1_input():
    assert solve("9,12,1,4,17,0,18", 2020) == 610


@pytest.mark.skip
def test_part2_small():
    assert solve("0,3,6", 30000000) == 175594
