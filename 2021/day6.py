#!/usr/bin/python

import sys
from collections import deque

file_path = str(sys.argv[1])
f = open(file_path, 'r')
content = f.read()
lanterns = map(lambda x: int(x), content.split(','))

# Part 1
for n in range(80):
    next_lanterns = []
    new_lanterns_count = 0
    for lantern in lanterns:
        if lantern == 0:
            next_lanterns.append(6)
            new_lanterns_count += 1
        else:
            next_lanterns.append(lantern - 1)
    for i in range(new_lanterns_count):
        next_lanterns.append(8)
    lanterns = next_lanterns[:]
print(len(lanterns))

# Part 2
lanterns = map(lambda x: int(x), content.split(','))
lanterns_histogram = deque([0 for _ in range(9)])
for lantern in lanterns:
    lanterns_histogram[lantern] += 1
for day in range(256):
    parent = lanterns_histogram.popleft()
    lanterns_histogram.append(parent)
    lanterns_histogram[6] += parent
print(sum(lanterns_histogram))
