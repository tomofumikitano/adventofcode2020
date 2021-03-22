#!/usr/bin/env python3
from day13 import build_bus_list, load_input, part1, part2


def test_part1_small():
    departure, bus_list = load_input("small.txt")
    assert part1(departure, bus_list) == 295


def test_part1_input():
    departure, bus_list = load_input("input.txt")
    assert part1(departure, bus_list) == 1895


def test_part2_small1():
    departure, bus_list = load_input("small.txt")
    assert part2(departure, bus_list) == 1068781


def test_part2_small2():
    departure, bus_list = load_input("small.txt")
    assert part2(departure, build_bus_list("17,x,13,19")) == 3417


def test_part2_small3():
    departure, bus_list = load_input("small.txt")
    assert part2(departure, build_bus_list("67,7,59,61")) == 754018


def test_part2_small4():
    departure, bus_list = load_input("small.txt")
    assert part2(departure, build_bus_list("67,7,x,59,61")) == 1261476


def test_part2_small5():
    departure, bus_list = load_input("small.txt")
    assert part2(departure, build_bus_list("1789,37,47,1889")) == 1202161486


def test_part2_input():
    departure, bus_list = load_input("input.txt")
    assert part2(departure,  bus_list, earliest=100000000000000) == 840493039281088 


