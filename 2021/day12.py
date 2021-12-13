#!/usr/bin/python

import sys
from collections import deque

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()

graph = {}

# Build graph
for row in rows:
    left, right = row.split('-')
    if left in graph:
        graph[left].append(right)
    else:
        graph[left] = [right]


def get_neighbors(node, graph, path):
    if node == 'end':
        return []
    return [x for x in graph[node] if x not in path or x.isupper()]


# Part 1
solutions = []
to_explore = deque(['start'])
current_solution = []
while to_explore:
    current_node = to_explore.popleft()
    current_solution.append(current_node)
    if current_node is 'end':
        solutions.append(current_solution)
        continue
    neighbors = get_neighbors(current_node, graph, current_solution)
    if not neighbors:
        current_solution.pop()
        continue

