#!/usr/bin/env python3
from itertools import product
from collections import defaultdict
from queue import Queue
import math


class Tile:

    def __init__(self, data):
        lines = data.strip().split("\n")
        self.id = int(lines[0].replace('Tile ', '').replace(':', ''))
        self.raw = lines[1:]
        self.neibours = {'N': None, 'S': None, 'E': None, 'W': None}
        self.rotation = 0
        self.flipped = False

    @property
    def edges(self):
        d = {}
        d["N"] = self.raw[0]
        d["S"] = self.raw[9]
        d["W"] = ''.join([self.raw[row][0] for row in range(10)])
        d["E"] = ''.join([self.raw[row][9] for row in range(10)])
        return d

    @property
    def edges_with_reversed(self):
        result = []
        for e in self.edges.values():
            result.append(e)
            result.append(e[::-1])
        assert len(result) == 8
        return result

    def rotate(self):
        rotated = []
        for col in range(10):
            line = ''.join(self.raw[row][col] for row in range(9, -1, -1))
            rotated.append(line)
        self.raw = rotated
        self.rotation += 1
        return self

    def flip(self):
        flipped = []
        for row in range(10):
            line = ''.join(self.raw[row][col] for col in range(9, -1, -1))
            flipped.append(line)
        self.raw = flipped
        self.flipped = not self.flipped
        return self

    def __repr__(self):
        return f"Tile(id={self.id}, )"

    def __str__(self):
        return '\n'.join(self.raw) + '\n'


def load_input(input_file):
    lookup = {}
    data = open(input_file).read().split("\n\n")
    for datam in data:
        tile = Tile(datam)
        lookup[tile.id] = tile
    return lookup


def find_tiles_in_corner(tiles):
    edge_counter = defaultdict(int)
    for _id, tile in tiles.items():
        for edge in tile.edges_with_reversed:
            edge_counter[edge] += 1

    unmatching_edges = {edge for edge, count in edge_counter.items()
                        if count == 1}

    # print(
    #     f"Total: {len(unmatching_edges)} unmatching edges:\n{unmatching_edges}")

    corner_tiles = {tile_id for tile_id, tile in tiles.items() if len(
        set.intersection(set(tile.edges_with_reversed), unmatching_edges)) == 4}
    print(f"Tiles in Corner: {corner_tiles}")

    return corner_tiles


def part1(input_file):
    tiles = load_input(input_file)
    return math.prod(find_tiles_in_corner(tiles))


def build_edge_to_tile_map(tiles):
    result = defaultdict(set)
    for _id, tile in tiles.items():
        for edge in tile.edges_with_reversed:
            result[edge].add(_id)
    return result


# def count_hash(tile):
#     return sum(tile.raw[i][j] == '#' for i in range(1, 9) for j in range(1, 9))

def match(tiles, id1: int, id2: int):
    print(f"Matching {id1} and {id2}")
    t1 = tiles[id1]
    t2 = tiles[id2]

    operations = 0
    while operations < 8:
        for (d1, d2) in [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]:
            if t1.neibours[d1] == None and t2.neibours[d2] == None and t1.edges[d1] == t2.edges[d2]:
                print(f" Matched {id1}_{d1} == {id2}_{d2}")
                t1.neibours[d1] = t2
                t2.neibours[d2] = t1
                return id2

        if not t2.flipped and t2.rotation == 3:
            t2.rotate()
            t2.flip()
        else:
            t2.rotate()

        operations += 1

    return None


def part2(input_file):

    tiles = load_input(input_file)

    tiles_in_corner = find_tiles_in_corner(tiles)
    edge_to_tile = build_edge_to_tile_map(tiles)

    # Get 1 of tile_in_corder for starter
    first = next(iter(tiles_in_corner))
    queue = Queue()
    queue.put(first)

    done = set()

    while not queue.empty():
        print(f"\nProcessing {tid}")
        for e in tiles[tid].edges.values():
            tiles_with_matching_edges = edge_to_tile[e] - {tid}
            for other in tiles_with_matching_edges - done:
                new_id = match(tiles, tid, other)
                # print(f" Putting {new_id} into queue")
                queue.put(new_id)
        done.add(tid)

    return 


if __name__ == "__main__":
    print("Part 1:", part1("input.txt"))
    # print("Part 2:", part2("input.txt"))
