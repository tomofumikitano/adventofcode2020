#!/usr/bin/env python3
import re
import sys
import time
import networkx as nx
# from networkx.algorithms.dag import topological_sort

ROOT_BAG = "shiny gold bag"


def parse_line(line):
    matches = re.match(r"^(.*)\ contain\ (.*)$", line)
    containing_bag, rest_of_string = matches.groups()
    containing_bag = containing_bag.rstrip("s")
    contained_bags = [(int(n), x.rstrip("s")) for n, x, _ in re.findall(
        r"([0-9]+)\ ([^\,\.]*)(\,|\.)", rest_of_string)]
    # print(containing_bag, contained_bags)
    return containing_bag, contained_bags

# graph where edge (x, y) with weight w means:
# w bags of x are contained in bag y
def build_containment_graph(data):
    lines = data.split("\n")
    bag_containment = [*map(parse_line, lines)]
    edges = ((bag, containing_bag, n)
             for (containing_bag, contained_bags) in bag_containment
             for (n, bag) in contained_bags)
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    return G


def part1(G):
    bfs = nx.bfs_tree(G, ROOT_BAG)
    # print(bfs)
    return len(bfs) - 1

if __name__ == "__main__":
    start = time.time()
    filename = "./input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    data = open(filename).read().strip()
    G = build_containment_graph(data) 
    print(f"Build Graph:   {time.time() - start}s")
    res = part1(G)
    print(f"Part 1: {res:5}, {time.time() - start}s")
