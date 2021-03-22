#!/usr/bin/env python3
import re
import sys
import time

RE_INNER_BAG = re.compile(r"^\s*(\d+)\s(.+)\sbag.*")
RE_BAG = re.compile(r"^(.+) bags contain (.+)")


def scan_bags(input_file):
    bags = {}
    for line in open(input_file):
        match = RE_BAG.match(line)
        outer, inner_bags = match[1], scan_inner_bags(match[2])
        bags[outer] = inner_bags
    return bags


def scan_inner_bags(input_inner):
    inner_bags = []
    for bag in input_inner.split(','):
        match = RE_INNER_BAG.match(bag.strip())
        if match:
            bag_count = int(match[1])
            bag_color = match[2]
        else:
            bag_count = 0
            bag_color = 'no other'
        inner_bags.append((bag_color, int(bag_count)))
    return inner_bags


def part1(bags, c):

    def contains(bags, c1, c2):
        if bags[c1] == [('no other', 0)]:
            return False
        if any(bag[0] == c2 for bag in bags[c1]):
            return True
        else:
            return any(contains(bags, bag[0], c2) for bag in bags[c1])

    return sum(contains(bags, c, 'shiny gold') for c in bags.keys())


# def part1(bags, c):
#
#     def directory_contains(bags, c1, c2):
#         return any([ bag[0] == c2 for bag in bags[c1] ])
#
#     result = {}
#
#     result = { bag for bag in bags if directory_contains(bags, bag, c) } 
#     print(f"{len(result)} bags contain {c}")
#
#     result.union({ bag for bag in bags if directory_contains(bags, bag.key(), ) })
#     bags_contain_bags_contain_shiny_gold = [ bag for bag in result if directory_contains(bags, bag, c) ] 
#     print(f"{len(bags_contain_bags_contain_shiny_gold)} bags contain {c}")
#
#     def contains(bags, c1, c2):
#         if bags[c1] == [('no other', 0)]:
#             return False
#         if any(bag[0] == c2 for bag in bags[c1]):
#             return True
#         else:
#             return any(contains(bags, bag[0], c2) for bag in bags[c1])
#
#     return sum(contains(bags, c, 'shiny gold') for c in bags.keys())


def part2(bags, my_color):

    def count_inner_bags(bags, my_color):
        if bags[my_color] == [('no other', 0)]:
            return 0
        return sum(bag[1] + bag[1] * count_inner_bags(bags, bag[0]) for bag in bags[my_color])

    return count_inner_bags(bags, my_color)


if __name__ == "__main__":

    input_file = "./bigboy.txt"
    start = time.time()

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    bags = scan_bags(input_file)

    print(f"Scan bags:     {time.time() - start}s")
    print(f"{len(bags.keys())} colors found")
    print(f"Part 1: {part1(bags, 'shiny gold'):5}, {time.time() - start}s")
    print(f"Part 2: {part2(bags, 'shiny gold'):5}, {time.time() - start}s")
