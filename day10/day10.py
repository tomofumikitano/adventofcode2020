#!/usr/bin/env python3
from collections import defaultdict


def load_adapters(filename):
    adapters = [0]  # Outlet
    with open(filename) as f:
        for line in f:
            adapters.append(int(line.strip()))
    adapters.append(max(adapters) + 3)  # Device

    list.sort(adapters)
    return adapters


def build_diffs(adapters):
    return [adapters[i+1] - adapters[i] for i in range(len(adapters) - 1)]


def part1(adapters):
    diffs = build_diffs(adapters)
    ones = [d == 1 for d in diffs]
    threes = [d == 3 for d in diffs]
    return sum(ones) * sum(threes)


def part2(adapters):
    # print(adapters)

    dp = defaultdict(int)
    dp[0] = 1

    for j in adapters:
        if dp[j] == 0:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    return dp[max(adapters)]


if __name__ == "__main__":
    # filename = "input.txt"
    # adapters = load_adapters(filename)
    # print(part2(adapters))

    adapters = load_adapters("./d16py1.txt")
    print(part2(adapters))
