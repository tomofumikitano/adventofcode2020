#!/usr/bin/env python3
import re

REQURED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_valid_part1(p: set):
    return REQURED_FIELDS.issubset(p.keys())


def is_valid_number(p: set, key: str, _min: int, _max: int):
    return key in p and _min <= int(p[key]) <= _max


def is_valid_height(p: set):
    return 'hgt' in p and \
        (p['hgt'][-2:] == "cm" and 150 <= int(p['hgt'][:-2]) <= 193 or
         p['hgt'][-2:] == "in" and 59 <= int(p['hgt'][:-2]) <= 76)


def is_valid_hair_color(p: set):
    return 'hcl' in p and bool(re.match("#[0-9a-f]{6}$", p['hcl']))


def is_valid_eye_color(p: set):
    return 'ecl' in p and p['ecl'] in VALID_EYE_COLORS


def is_valid_passport_id(p: set):
    return 'pid' in p and bool(re.match("^[0-9]{9}$", p['pid']))


def is_valid_part2(p: set):
    return is_valid_number(p, 'byr', 1920, 2002) and \
        is_valid_number(p, 'iyr', 2010, 2020) and \
        is_valid_number(p, 'eyr', 2020, 2030) and \
        is_valid_height(p) and \
        is_valid_hair_color(p) and \
        is_valid_eye_color(p) and \
        is_valid_passport_id(p)


def solve(_input="input4.txt", is_valid=is_valid_part1):

    records = [record.replace("\n", " ").split(" ") for record in open(_input).read().strip().split("\n\n")]
    passports = [ { field.split(":")[0]:field.split(":")[1] for field in record } for record in records ]

    valid_count = 0
    for passport in passports:
        valid_count += is_valid(passport)

    print(f"Found {len(passports)} passports, {valid_count} valid passports")


if __name__ == "__main__":
    fname = "./big_boy_day4.txt"
    # solve(_input=fname, is_valid=is_valid_part1)
    solve(_input=fname, is_valid=is_valid_part2)
