#!/usr/bin/env python3
import pytest
from day14 import part1, part2


def test_part1_small1():
    assert part1("./small.txt") == 165


def test_part1_input():
    assert part1("./input.txt") == 7611244640053


def test_part1_bigboy1():
    assert part1("./qh9d5y") == 16843575639443


# def test_build_mask_list():
#     assert list(build_mask_list("1")) == ["1"]
#     assert list(build_mask_list("0")) == ["0"]
#     assert list(build_mask_list("X")) == ['0', '1']
#     assert list(build_mask_list("0X")) == ['00', '01']
#     assert list(build_mask_list("X0")) == ['00', '10']
#     assert list(build_mask_list("X0X")) == ['000', '001', '100', '101']


def test_part2_small2():
    assert part2("./small2.txt") == 208


def test_part2_input():
    assert part2("./input.txt") == 3705162613854


@pytest.mark.skip("Not tested yet")
def test_part2_bigboy1():
    assert part2("./qh9d5y") == 13155495224492902966
