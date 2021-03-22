#!/usr/bin/env python3
from collections import deque
import math


def solve1(line, start=0):
    line = line.rstrip()
    stack = deque()
    i = start
    while i < len(line):
        c = line[i]

        if c == ' ':
            i += 1
            continue

        if c in '+*':
            stack.append(c)
        else:
            if c == ')':
                return stack.pop(), i
            elif c == '(':
                op, i = solve1(line, start=i+1)
            else:
                op = int(c)

            if len(stack) > 0 and stack[-1] in '+*':
                operator = stack.pop()
                if operator == '*':
                    stack.append(op * stack.pop())
                elif operator == '+':
                    stack.append(op + stack.pop())
            else:
                stack.append(op)
        # print(stack)
        i += 1
    return stack.pop()


def part1(input_file):
    return sum(map(solve1, open(input_file)))


def solve2(line, start=0):
    line = line.rstrip()

    def prod_stack_items(stack):
        return math.prod([x for x in stack if type(x) == int])

    stack = deque()
    i = start
    while i < len(line):
        c = line[i]

        if c == ' ':
            i += 1
            continue

        if c in '+*':
            stack.append(c)
        else:
            if c == ')':
                return prod_stack_items(stack), i
            elif c == '(':
                op, i = solve2(line, start=i+1)
            else:
                op = int(c)

            if len(stack) > 0 and stack[-1] in {'+'}:
                operator = stack.pop()
                if operator == '+':
                    stack.append(op + stack.pop())
            else:
                stack.append(op)

        i += 1

    # print(stack)
    return prod_stack_items(stack)


def part2(input_file):
    return sum(map(solve2, open(input_file)))


if __name__ == "__main__":
    # print(solve2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
    # print(solve2("1 + 2 * 3 + 4"))
    # print(part2("input.txt"))
    pass
