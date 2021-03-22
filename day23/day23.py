#!/usr/bin/env python3
from __future__ import annotations
from typing import Dict, List, Optional


class Cup:

    def __init__(self, value):
        self.value = value
        self.next: Cup = None

    def __repr__(self) -> str:
        return f"{self.value}"

    def __str__(self) -> str:
        return f"{self.value}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cup):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


def print_cups(cups: List[Cup], current: Cup) -> str:
    result = f"({current.value}) "
    cup = current.next
    while cup != current:
        result += str(cup.value) + " "
        cup = cup.next
    return result.rstrip()


def run(cups: List[Cup], lookup: Dict[int, Cup], moves):
    for i in range(len(cups) - 1):
        cups[i].next = cups[i+1]

    cups[len(cups) - 1].next = cups[0]
    current: Cup = cups[0]
    min_val = min(lookup.keys())
    max_val = max(lookup.keys())

    def find_destination(cups, current, picked_up, lookup):
        picked_up_values = {p.value for p in picked_up}
        dest_val = current.value - 1
        if dest_val < min_val:
            dest_val = max_val
        while dest_val in picked_up_values:
            dest_val -= 1
            if dest_val < min_val:
                dest_val = max_val
        return lookup[dest_val]

    for i in range(1, moves + 1):
        picked_up: List[Cup] = [current.next,
                                current.next.next,
                                current.next.next.next]
        destination = find_destination(cups, current, picked_up, lookup)

        # print(f"-- move {i + 1} --")
        # print(f"cups: {print_cups(cups, current)}")
        # print(f"pick up: {picked_up}")
        # print(f"destination: {destination.value}")
        # print()
        current.next = picked_up[2].next
        picked_up[2].next = destination.next
        destination.next = picked_up[0]
        current = current.next


def part1(_input, moves=100) -> Optional[str]:

    def build_ans_part1(lookup: Dict[int, Cup]):
        current = lookup[1].next
        result = ""
        while current.value != 1:
            result += str(current.value)
            current = current.next
        return int(result)

    cups = [Cup(int(x)) for x in _input]
    lookup: Dict[int, Cup] = {cup.value: cup for cup in cups}

    run(cups, lookup, moves)
    # print(f"final: {print_cups(cups, current)}")
    return build_ans_part1(lookup)


def part2(_input, moves=10000000):

    def build_ans_part2(lookup: Dict[int, Cup]):
        cup = lookup[1]
        return cup.next.value * cup.next.next.value

    cups = [Cup(int(x)) for x in _input]
    for i in range(10, 1000001):
        cups.append(Cup(i))
    assert len(cups) == 1000000
    lookup: Dict[int, Cup] = {cup.value: cup for cup in cups}

    run(cups, lookup, moves)
    return build_ans_part2(lookup)


if __name__ == "__main__":
    # print(part2("389125467", 10000000))
    print(part2("653427918", 10000000))
