#!/usr/bin/env python3
import pytest
from day11 import build_grid, solve, count_occupied_visible, visible_seats


def test_part1_small():
    grid = build_grid("small.txt")
    assert 37 == solve(grid)


# @pytest.mark.skip
def test_part1_input():
    grid = build_grid("input.txt")
    assert 2368 == solve(grid)


def test_visible_seats():
    g1 = build_grid("./part2_1.txt")
    seats = visible_seats(g1, 4, 3)
    num_seats = sum([len(l) for l in seats])
    assert 30 == num_seats

    g2 = build_grid("./part2_2.txt")
    seats = visible_seats(g2, 1, 1)
    num_seats = sum([len(l) for l in seats])
    assert 18 == num_seats

    g3 = build_grid("./part2_3.txt")
    seats = visible_seats(g3, 3, 3)
    num_seats = sum([len(l) for l in seats])
    assert 24 == num_seats


def test_occupied_visible():
    assert count_occupied_visible(build_grid("./part2_1.txt"), 4, 3) == 8
    assert count_occupied_visible(build_grid("./part2_2.txt"), 1, 1) == 0
    assert count_occupied_visible(build_grid("./part2_3.txt"), 3, 3) == 0


def test_part2_small():
    grid = build_grid("small.txt")
    assert 26 == solve(grid, count_occupied_visible, threshold=5)


def test_part2_input():
    grid = build_grid("input.txt")
    assert 2124 == solve(grid, count_occupied_visible, threshold=5)
