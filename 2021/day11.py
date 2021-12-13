#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()

octopuses = [[int(x) for x in row] for row in rows]
width, height = len(octopuses[0]), len(octopuses)


def get_neighbors(location, width, height):
    neighbors = []
    for o_y in [-1, 0, 1]:
        for o_x in [-1, 0, 1]:
            if o_x == 0 and o_y == 0:
                continue
            neighbors.append((location[0] + o_x, location[1] + o_y))
    neighbors = list(filter(lambda x: 0 <= x[0] < width and 0 <= x[1] < height, neighbors))
    return neighbors


def increment(location, octopuses, flashes):
    octopuses[location[1]][location[0]] += 1
    if octopuses[location[1]][location[0]] == 10:
        child_flashes = 0
        for neighbor in get_neighbors(location, width, height):
            child_flashes += increment(neighbor, octopuses, flashes)
        return 1 + child_flashes
    else:
        return 0


# return new octopuses config and flash count
def step(octopuses):
    flashes = 0
    for y, row in enumerate(octopuses):
        for x, octopus in enumerate(row):
            flashes += increment((x, y), octopuses, flashes)
    for y, row in enumerate(octopuses):
        for x, octopus in enumerate(row):
            octopuses[y][x] = 0 if octopuses[y][x] > 9 else octopuses[y][x]
    return flashes


flashes_sum = 0
i = 0
while True:
    i += 1
    current_flash = step(octopuses)
    flashes_sum += current_flash
    if i == 100:
        # Part 1
        print(flashes_sum)
    if current_flash == 100:
        # Part 2
        print(i)
        break
