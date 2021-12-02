#!/usr/bin/python
import sys

file_path = str(sys.argv[1])
depth = 0
h_position = 0
aim = 0
with open(file_path) as rows:
    for row in rows:
        cat, value = row.split()
        if cat == 'forward':
            h_position += int(value)
            depth += aim * int(value)
        elif cat == 'up':
            aim -= int(value)
        elif cat == 'down':
            aim += int(value)
        else:
            raise Exception(f'Unknown {cat}')
print(depth * h_position)
