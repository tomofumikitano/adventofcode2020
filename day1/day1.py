#!/usr/bin/env python3
import time
import sys


def part1(fname="input.txt", target=2020):
    numbers = set()
    with open(fname) as f:
        for line in f:
            number = int(line.strip())
            if target - number in numbers:
                print(
                    f"Part1: {number} * {target - number} = {number * (target - number)}")
            else:
                numbers.add(number)


def part2(fname="input.txt", target=2020):
    print(f"Running Part2 with {fname}, {target}")
    num_list = []
    num_set = set()
    with open(fname) as f:
        for line in f:
            num_set.add(int(line.strip()))
        num_list = sorted(num_set)

        for i in range(len(num_list) - 2):
            for j in range(i + 1, len(num_list) - 1):
                if num_list[i] + num_list[j] < target:
                    remainder = target - num_list[i] - num_list[j]
                    if remainder in num_set and num_list[j] < remainder:
                        ans = num_list[i] * num_list[j] * remainder
                        return f"Part2: {num_list[i]} + {num_list[j]} + {remainder} = {target}, Ans = {ans}"


def timer(func, *args):
    print(f"Running {func.__name__} with parameter {args}")
    start = time.time()
    print(func(*args))
    end = time.time()
    print(f"runtime: {int(end - start)}s")


if __name__ == "__main__":
    fname = "./gy8n81.txt"
    # fname = "./1qwlzz.txt"
    target = 99920044

    if len(sys.argv) > 2:
        fname = sys.argv[1]
        target = int(sys.argv[2])

    timer(part2, fname, target)
