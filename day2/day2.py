#!/usr/bin/env python3
from collections import Counter


def is_valid_part1(i, j, letter, password):
    counter = Counter(password)
    count = counter[letter]
    if i <= count and count <= j:
        return True
    # print(f"Analyzing {i}, {j}, {letter}, {password}")
    # print(f"{letter} appears {count} times")
    # print(f"counter = {counter}")
    return False 


def is_valid_part2(i, j, letter, password):
    if (password[i - 1] == letter and password[j - 1] != letter) or \
            (password[i - 1] != letter and password[j - 1] == letter):
        return True
    # print(f"Analyzing {i}, {j}, {letter}, {password}")
    # print(f"password[{i}] = {password[i-1]}, password[{j}] = {password[j-1]}")
    return False 


def solve(part=1, input="input.txt", validate=is_valid_part1):
    valid_passwords = 0
    with open(input) as f:
        for line in f:
            (min_max, letter, password) = line.strip().split(" ")
            (i, j) = min_max.split("-")
            (i, j) = (int(i), int(j))
            letter = letter.replace(':', '')
            if validate(i, j, letter, password):
                valid_passwords += 1
    # print(f"Part {part}: Found {valid_passwords} valid password")
    return valid_passwords


if __name__ == "__main__":
    # TODO - Is it possible to embed property 'name' in validate function so you can call solve() like this?
    print(solve(part=1, input="input.txt", validate=is_valid_part1))
    print(solve(part=2, input="input.txt", validate=is_valid_part2))
