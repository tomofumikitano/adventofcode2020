#!/usr/bin/env python3
import pytest
from day25 import part1, find_loop


def test_find_loop():
    assert find_loop(5764801) == 8


def test_part1_small():
    assert part1(5764801, 17807724) == 14897079


def test_part1_input():
    assert part1(15113849, 4206373) == 1890859
