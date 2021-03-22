#!/usr/bin/env python3

def load_input(filename, bigboy=False):
    numbers = []
    with open(filename) as f:
        for line in f:
            if line.strip().startswith("ABBERATION:"):
                pass
            else:
                numbers.append(int(line))
    return numbers


def part1(numbers, preamble_size=25):

    def has_combination(numbers, target, lo, hi):
        for i in range(lo, hi):
            if (target - numbers[i]) in numbers[lo:hi+1]:
                return True
        return False

    for i in range(preamble_size, len(numbers)):
        target = numbers[i]
        if not has_combination(numbers, target, i - preamble_size, i - 1):
            return (numbers[i], i)


def part2(numbers, index, target):

    front, sum_total = 0, 0
    for back in range(len(numbers)):

        while (front < len(numbers) and sum_total + numbers[front] <= target):
            sum_total += numbers[front]
            front += 1

        if sum_total == target:
            return (min(numbers[back:front]) + max(numbers[back:front]), numbers[back:front])

        sum_total -= numbers[back]

    raise Exception("Huh?")


def test_small_input():
    numbers = load_input("./input_small.txt")
    invalid_number, index = part1(numbers, 5)
    assert invalid_number == 127
    ans, sublist = part2(numbers, index, invalid_number)
    # print(invalid_number, ans, sublist)
    assert ans == 62


def test_input():
    numbers = load_input("./input.txt")
    invalid_number, index = part1(numbers, 25)
    assert invalid_number == 27911108
    ans, sublist = part2(numbers, index, invalid_number)
    # print(invalid_number, ans, sublist)
    assert ans == 4023754


if __name__ == "__main__":

    # Big Boy
    filename, bigboy = "./bigboy_10000.txt", True

    numbers = load_input(filename, bigboy=bigboy)
    invalid_number, index = part1(numbers)
    print(f"Part 1: {invalid_number} at {index}")

    (ans, sublist) = part2(numbers, index, invalid_number)
    print(f"Part 2: {ans}, {len(sublist)}, {sublist}")
