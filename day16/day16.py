#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from typing import List, Dict


def load_data(input_file: str):

    rules: dict = dict()
    your_ticket = []
    nearby_tickets = []

    SECTION_RULES = 0
    SECTION_YOUR_TICKET = 1
    SECTION_NEARBY_TICKETS = 2

    with open(input_file) as f:

        section = SECTION_RULES

        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue

            if line == "your ticket:":
                section = SECTION_YOUR_TICKET
            elif line == "nearby tickets:":
                section = SECTION_NEARBY_TICKETS
            elif section == SECTION_RULES:
                k, v = line.split(': ')
                ranges: List[range] = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1)
                     for x in v.split(" or ")]
                rules[k] = ranges 
            elif section == SECTION_YOUR_TICKET:
                your_ticket = list(map(int, line.split(',')))
            elif section == SECTION_NEARBY_TICKETS:
                nearby_tickets.append(list(map(int, line.split(','))))

    rules_flat = [item for elem in rules.values() for item in elem]
    return rules, rules_flat, your_ticket, nearby_tickets


def is_valid(v: int, rules_flat: List[range]):
    # 少なくともいずれかのルールにマッチしている
    for rule in rules_flat:
        if v in rule:
            return True
    return False


def find_valid_tickets(nearby_tickets: List[List[int]], rules_flat: List[range]):
    valid_tickets = []
    for ticket in nearby_tickets:
        if all([is_valid(v, rules_flat) for v in ticket]):
            valid_tickets.append(ticket)
    return valid_tickets


def part1(input_file: str):
    rules, rules_flat, your_ticket, nearby_tickets = load_data(input_file)
    result = 0
    for ticket in nearby_tickets:
        for v in ticket:
            if not is_valid(v, rules_flat):
                result += v
    return result


def part2(input_file: str):
    rules, rules_flat, your_ticket, nearby_tickets = load_data(input_file)

    valid_tickets = find_valid_tickets(nearby_tickets, rules_flat)
    valid_tickets.append(your_ticket)

    field_columns_map = defaultdict(set)
    for rule, ranges in rules.items():
        for col in range(len(your_ticket)):
            if all(v in ranges[0] or v in ranges[1] for v in [ticket[col] for ticket in valid_tickets]):
                field_columns_map[rule].add(col)

    for k, v in field_columns_map.items():
        print(k, v)

    field_column_map: Dict[str, int] = dict()

    while len(field_column_map) < len(your_ticket):
        for field, columns in field_columns_map.items():
            if len(columns) == 1:
                column = columns.pop()
                field_column_map[field] = column
                for l in field_columns_map:
                    if l != field and column in field_columns_map[l]:
                        field_columns_map[l].remove(column)

    for f, c in field_column_map.items():
        print(f, c)

    indices = [v for k, v in field_column_map.items()
               if k.startswith("departure")]
    result = reduce(lambda x, y: x * y, [your_ticket[i] for i in indices], 1)
    return result


if __name__ == "__main__":
    print(part2("input.txt"))
