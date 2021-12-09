#!/usr/bin/python

import sys


def wind_path(coord):
    x1 = int(coord[0][0])
    x2 = int(coord[1][0])
    y1 = int(coord[0][1])
    y2 = int(coord[1][1])
    x_step = 1 if x1 <= x2 else -1
    y_step = 1 if y1 <= y2 else -1
    x_values = list(range(x1, x2 + x_step, x_step))
    y_values = list(range(y1, y2 + y_step, y_step))
    if len(x_values) < len(y_values):
        x_values = [x_values[0] for _ in range(len(y_values))]
    elif len(x_values) > len(y_values):
        y_values = [y_values[0] for _ in range(len(x_values))]
    paths = list(zip(x_values, y_values))
    return paths


file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()
winds = [[x.split(',') for x in row.split(' -> ')] for row in rows]

# Part 1
#winds_candidate = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], winds))

# Part 2
winds_candidate = winds[:]

winds_map = {}
for wind in winds_candidate:
    paths = wind_path(wind)
    for path in paths:
        if path in winds_map:
            winds_map[path] = 1
        else:
            winds_map[path] = 0
print(sum(list(winds_map.values())))
