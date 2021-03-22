#!/usr/bin/env python3
import re

RULES = 0
MESSAGES = 1


def load_input(input_file):

    section = RULES
    rules = {}
    messages = []
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                section = MESSAGES
            elif section == RULES:
                k, v = line.split(':')
                k = int(k)
                v = v.strip().replace('"', '').split(" ")
                rules[k] = v
            elif section == MESSAGES:
                messages.append(line)
            else:
                raise Exception(f"Unexpected: {line}")
    return rules, messages


def build_pattern(rules, i=0):
    pattern = ''

    parenthesis = False
    if '|' in rules[i]:
        pattern += '('
        parenthesis = True

    for c in rules[i]:
        if c in '|+' or c.isalpha():
            pattern += c
        elif c.isnumeric():
            pattern += build_pattern(rules, int(c))
        else:
            raise NotImplementedError(f"Huh?: {c}")

    if parenthesis:
        pattern += ')'

    return pattern


def part1(input_file):
    rules, messages = load_input(input_file)
    pattern = build_pattern(rules)
    regex = re.compile('^' + pattern + '$')

    return sum(bool(regex.match(message)) for message in messages)


def part2(input_file, repeat=5):
    rules, messages = load_input(input_file)

    # rules[8] = ['42', '|', '42', '8']
    rules[8] = ['42', '+']

    # rules[11] = ['42', '31', '|', '42', '11', '31']
    rules[11] = []
    for i in range(1, repeat):
        for _ in range(i):
            rules[11].append('42')
        for _ in range(i):
            rules[11].append('31')
        rules[11].append('|')

    rules[11] = rules[11][:-1]

    pattern = build_pattern(rules)
    regex = re.compile('^' + pattern + '$')

    return sum(bool(regex.match(message)) for message in messages)


if __name__ == "__main__":
    print(part1("./input.txt"))
    # for i in range(10):
    #     print(part2("./input.txt", repeat=i))
