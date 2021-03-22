#!/usr/bin/env python3
from math import lcm


def load_input(filename):
    with open(filename) as f:
        departure = int(f.readline())
        bus_list = f.readline().strip().split(',')
        return departure, bus_list


def build_bus_list(line: str):
    return line.split(",")


def part1(departure, bus_list):

    def find_earliest_bus_and_time(departure, bus_list):
        bus_list = [int(x) for x in bus_list if x != 'x']
        t = departure
        cont = True
        while cont:
            for bus in bus_list:
                if t % bus == 0:
                    return t, bus
                    cont = False
                    break
            t += 1

    t, bus = find_earliest_bus_and_time(departure, bus_list)
    return (t - departure) * bus


def part2(departure, bus_list, earliest=0, debug=False):
    m = {offset: int(id) for offset, id in enumerate(bus_list) if id != 'x'}
    print(f"{len(m)} buses, {m}")

    t = earliest

    LCM = 1 
    print(f"Starting t = {t}")
    while True:
        print(f"Checking = {t}")
        for offset, bus_id in m.items():
            if (t + offset) % bus_id == 0:
                LCM = lcm(LCM, bus_id)
                pass
            else:
                break
        if all((t + offset) % bus_id == 0 for offset, bus_id in m.items()):
            print(t, t, m)
            return t
        t += LCM


if __name__ == "__main__":
    departure, bus_list = load_input("input.txt")
    print(part2(departure,  bus_list, earliest=100000000000000))
