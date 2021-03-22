#!/usr/bin/env python3
# import pytest
from day21 import part1, part2


def test_part1_small():
    assert part1("small.txt") == 5


def test_part1_input():
    assert part1("input.txt") == 2659


def test_part2_small():
    assert part2("small.txt") == 'mxmxvkd,sqjhc,fvjkl' 


def test_part2_input():
    assert part2("input.txt") == 'rcqb,cltx,nrl,qjvvcvz,tsqpn,xhnk,tfqsb,zqzmzl'
