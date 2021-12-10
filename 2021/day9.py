#!/usr/bin/python

import sys
from collections import deque

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()

height_map = [[int(c) for c in row] for row in rows]


# Part 1
def get_neighbors(x, y, matrix):
    candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    final = list(filter(lambda i: 0 <= i[0] < len(matrix[0]) and 0 <= i[1] < len(matrix), candidates))
    return final


def is_low(x, y, neighbors, matrix):
    current = matrix[y][x]
    neighbors_value = [matrix[x[1]][x[0]] for x in neighbors]
    return current < min(neighbors_value)


risk_level = 0
for y, row in enumerate(height_map):
    for x, col in enumerate(row):
        neighbors = get_neighbors(x, y, height_map)
        if is_low(x, y, neighbors, height_map):
            current = height_map[y][x]
            risk_level += 1 + current
print(risk_level)


# Part 2
# Return size, and new seen points
def get_basin(low_point, seen_points, matrix):
    cur_seen_points = seen_points.copy()
    to_explore_points = {low_point}
    size = 0
    while len(to_explore_points) > 0:
        cur_point = to_explore_points.pop()
        cur_seen_points.add(cur_point)
        size += 1
        neighbors = get_neighbors(cur_point[0], cur_point[1], matrix)
        neighbors = list(filter(lambda x: matrix[x[1]][x[0]] < 9, neighbors))
        neighbors = list(filter(lambda x: x not in cur_seen_points, neighbors))
        for item in neighbors:
            to_explore_points.add(item)
    return size, cur_seen_points


low_points = []
for y, row in enumerate(height_map):
    for x, col in enumerate(row):
        neighbors = get_neighbors(x, y, height_map)
        if is_low(x, y, neighbors, height_map):
            low_points.append((x, y))
seen_points = set()
basins_size = []
for low_point in low_points:
    basin_size, seen_points = get_basin(low_point, seen_points, height_map)
    basins_size.append(basin_size)
result = 1
for size in sorted(basins_size)[-3:]:
    result *= size
print(result)
