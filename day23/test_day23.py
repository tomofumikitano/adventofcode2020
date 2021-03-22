#!/usr/bin/env python3
from day23 import part1, part2
import pytest


def test_part1_10():
    assert part1("389125467", 10) == 92658374

def test_part1_100():
    assert part1("389125467", 100) == 67384529

def test_part1():
    assert part1("653427918", 100) == 76952348

@pytest.mark.skip(reason="SLOW")
def test_part2_sample():
    assert part2("389125467", 10000000) == 149245887792

def test_part2():
    assert part2("653427918", 10000000) == 72772522064
