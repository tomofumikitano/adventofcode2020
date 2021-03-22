#!/usr/bin/env python3
import pytest
from day16 import load_data, part1, part2

def test_part1_input():
    assert part1("input.txt") == 19070

def test_part2_input():
    assert part2("input.txt") == 161926544831
