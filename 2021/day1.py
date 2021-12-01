#!/usr/bin/python
import sys

file_path = str(sys.argv[1])
depths = []
with open(file_path) as rows:
    for row in rows:
        depths.append(int(row))

def increase_count(depths):
    increase_count = 0
    for i, depth in enumerate(depths[:-1]):
        if depth < depths[i+1]:
            increase_count += 1
    return increase_count

print(increase_count(depths))

window_size = 3
window_depths = []
for i in range(len(depths) - window_size + 1):
    window_depths.append(depths[i:i + window_size])
window_sum = [sum(x) for x in window_depths]

print(increase_count(window_sum))