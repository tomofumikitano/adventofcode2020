#!/usr/bin/env python3

MOVE = {
    'ne': (0, 1),
    'e': (1, 0),
    'se': (1, -1),
    'nw': (-1, 1),
    'w': (-1, 0),
    'sw': (0, -1),
}


def read_line(line):
    result = []
    line = line.strip()
    for i, c in enumerate(line):
        if c == "n" or c == "s":
            result.append(c)
        elif c == "e" or c == "w":
            if len(result) > 0 and result[-1] in "ns":
                result[-1] += c
            else:
                result.append(c)
    return result


def load_input(input_file):
    data = []
    with open(input_file) as f:
        for line in f:
            data.append(read_line(line))
    return data


def follow_instruction(instruction):
    x, y = 0, 0
    for d in instruction:
        x = x + MOVE[d][0]
        y = y + MOVE[d][1]
    return (x, y)


def flip_tiles(instructions):
    tiles = set()
    for i in instructions:
        tile = follow_instruction(i)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)
    return tiles


def part1(input_file):
    instructions = load_input(input_file)
    black_tiles = flip_tiles(instructions)
    return len(black_tiles)


def find_whites(blacks):
    whites = set()
    for tile in blacks:
        # print("Checking", tile)
        for delta in MOVE.values():
            neibour = (tile[0] + delta[0], tile[1] + delta[1])
            if neibour not in blacks:
                whites.add(neibour)
    return whites


def count_adjacent_blacks(tile, blacks):
    count = 0
    for delta in MOVE.values():
        if (tile[0] + delta[0], tile[1] + delta[1]) in blacks:
            count += 1
    return count


def black_to_black(blacks):
    new_black_tiles = set()
    for tile in blacks:
        count = count_adjacent_blacks(tile, blacks)
        if count == 0 or count > 2:
            pass
        else:
            new_black_tiles.add(tile)
    return new_black_tiles


def white_to_black(whites, blacks):
    new_black_tiles = set()
    for tile in whites:
        count = count_adjacent_blacks(tile, blacks)
        if count == 2:
            new_black_tiles.add(tile)
    return new_black_tiles


def part2(input_file, repeat=100):
    instructions = load_input(input_file)
    blacks = flip_tiles(instructions)

    for day in range(1, repeat+1):
        whites = find_whites(blacks)
        new_black_tiles = set.union(black_to_black(
            blacks), white_to_black(whites, blacks))
        # print(f"Day {day}: {len(new_black_tiles)}")
        blacks = new_black_tiles

    return len(blacks)


if __name__ == "__main__":
    print(part2("input.txt", 100))
    # print(part2("input.txt"))
