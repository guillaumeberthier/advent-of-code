#!/usr/bin/python

import sys
import heapq

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()
COST = [[int(x) for x in row] for row in rows]
MAX = 9999


def dijkstra(cost):
    d = {}
    width, height = len(cost[0]), len(cost)
    for row in range(height):
        for col in range(width):
            d[(col, row)] = MAX
    d[(0, 0)] = 0
    e = [(0, (0, 0))]
    heapq.heapify(e)
    off_neighs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while e:
        a = heapq.heappop(e)
        for off_neigh in off_neighs:
            x = a[1][0] + off_neigh[0]
            y = a[1][1] + off_neigh[1]
            if 0 <= x < width and 0 <= y < height and (x, y) and d[(x, y)] > d[a[1]] + cost[y][x]:
                d[(x, y)] = d[a[1]] + cost[y][x]
                heapq.heappush(e, (d[a[1]] + cost[y][x], (x, y)))
    return d[(width - 1, height - 1)]


print(dijkstra(COST))

GRID = [[x for x in row] for row in COST]
tilew = len(GRID)
tileh = len(GRID[0])

for _ in range(4):
    for row in GRID:
        tail = row[-tilew:]
        row.extend((x + 1) if x < 9 else 1 for x in tail)

for _ in range(4):
    for row in GRID[-tileh:]:
        row = [(x + 1) if x < 9 else 1 for x in row]
        GRID.append(row)

print(dijkstra(GRID))
