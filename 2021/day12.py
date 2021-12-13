#!/usr/bin/python

import sys

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
    if right in graph:
        graph[right].append(left)
    else:
        graph[right] = [left]


# Part 1
def get_neighbors(node, graph, visited_nodes):
    return [x for x in graph[node] if x not in visited_nodes or x.isupper()]


# Part 2
def get_neighbors_2(node, graph, visited_nodes):
    candidates = []
    for candidate in graph[node]:
        if candidate == 'start':
            continue
        elif candidate.isupper():
            candidates.append(candidate)
        elif candidate == 'end':
            candidates.append(candidate)
        elif visited_nodes.count(candidate) == 0:
            candidates.append(candidate)
        elif visited_nodes.count(candidate) == 1:
            twice_minus = [item for item in visited_nodes if visited_nodes.count(item) > 1 and item.islower() and item]
            if len(twice_minus) == 0:
                candidates.append(candidate)
    return candidates


solutions = set()


def get_all_paths(source, destination, graph, visited_nodes, path):
    visited_nodes.append(source)
    path.append(source)
    if source == destination:
        solutions.add(','.join(path))
        return
    neighbors = get_neighbors_2(source, graph, visited_nodes)
    for neighbor in neighbors:
        get_all_paths(neighbor, destination, graph, visited_nodes.copy(), path.copy())


get_all_paths('start', 'end', graph, [], [])
print(len(solutions))
