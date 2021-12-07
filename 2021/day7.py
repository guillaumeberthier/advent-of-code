#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
content = f.read()
crabs = list(map(lambda x: int(x), content.split(',')))

min, max = min(crabs), max(crabs)
min_dist = 999999999
for i in range(min, max+1):
    cur_dist = 0
    for crab in crabs:
        n = abs(i - crab)
        cost_part_1 = n
        cost_part_2 = n * (n + 1) / 2
        cur_dist += cost_part_2
    if min_dist > cur_dist:
        min_dist = cur_dist
print(min_dist)
