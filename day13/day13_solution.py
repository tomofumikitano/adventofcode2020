#!/usr/bin/env python3
from sympy.ntheory.modular import crt


def part1(time, depeatures):
    depeature_scores = sorted(((-time) % dep, dep) for _, dep in depeatures)
    # print("Sorted: ", depeature_scores)
    best_t, best_departure = depeature_scores[0]
    return best_t * best_departure


def part2(time, departures):
    ids, modules = zip(*departures)
    __import__('ipdb').set_trace()
    remainders = [-x for x in ids]
    result, _ = crt(modules, remainders)
    return int(result)


if __name__ == "__main__":
    time, depeature_string = open("small.txt").read().split()
    time = int(time)
    depeatures = [(i, int(x))
                  for i, x in enumerate(depeature_string.split(","))
                  if x != 'x']

    print(time)
    print(depeatures)

    # print(part1(time, depeatures))

    print(part2(time, depeatures))
