#!/usr/bin/env python3
from day10 import load_adapters, part1, part2


def test_part1_small1():
    adapters = load_adapters("small1.txt")
    assert part1(adapters) == 35


def test_part1_small2():
    adapters = load_adapters("small2.txt")
    assert part1(adapters) == 220


def test_part1_input1():
    adapters = load_adapters("input.txt")
    assert part1(adapters) == 2574


def test_part2_small1():
    adapters = load_adapters("small1.txt")
    assert part2(adapters) == 8


def test_part2_small2():
    adapters = load_adapters("small2.txt")
    assert part2(adapters) == 19208


def test_part2_input():
    adapters = load_adapters("input.txt")
    assert part2(adapters) == 2644613988352
