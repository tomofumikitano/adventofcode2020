#!/usr/bin/env python3
import curses
from curses import wrapper
import time

def count_trees(grid, dx, dy):
    num_trees = 0

    rows = len(grid)
    cols = len(grid[0])

    row, col = 0, 0
    while row < rows - 2:
        col = (col + dx) % cols
        row += dy
        yield (row, col)
        # assert row < rows
        # assert col < cols
        # if grid[row][col] == '#':
        #     num_trees += 1

    yield num_trees


def draw(stdscr, grid, dx, dy):
    screen_height = stdscr.getmaxyx()[0] 

    stdscr.clear()
    grid = [line.replace('#', '🎄') for line in grid]
    grid = [line.replace('.', '❄️ ') for line in grid]

    for i in range(0, screen_height):
        time.sleep(.02)
        stdscr.addstr(i, 0, grid[i])
        stdscr.refresh()

    stdscr.addstr(0, 0, '🏂')
    stdscr.refresh()
    stdscr.getkey()

    for (row, col) in count_trees(grid, dx, dy):
        if row == screen_height:
            return
        stdscr.addstr(row, col, '🏂')
        stdscr.refresh()
        stdscr.getkey()

    stdscr.getkey()


if __name__ == "__main__":
    grid = [line.strip() for line in open("input.txt")]

    # for x in count_trees(grid, dx=3, dy=1):
    #     print(x)

    stdscr = curses.initscr()
    wrapper(draw, grid, dx=3, dy=1)

    # for (row, col) in count_trees(grid, slope=(3, 1)):
    #     print(row, col)
