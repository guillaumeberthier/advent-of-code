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
    if right in graph:
        graph[right].append(left)
    else:
        graph[right] = [left]


# Part 1
def get_neighbors(node, graph, visited_nodes):
    return [x for x in graph[node] if x not in visited_nodes or x.isupper()]


# Part 2
def get_neighbors_2(node, graph, visited_nodes):
    forbidden_nodes = set()
    for visited_node in visited_nodes:
        if visited_nodes.count(visited_node) > 2:
            forbidden_nodes.add(visited_node)
    forbidden_nodes.add('start')
    twice_nodes = set(filter(lambda x: visited_nodes.count(x) == 2, visited_nodes))
    twice_nodes_scenarios = [twice_nodes.difference(x) for x in twice_nodes]
    if twice_nodes_scenarios:
        forbidden = [forbidden_nodes.union(x) for x in twice_nodes_scenarios]
        result = []
        for forb in forbidden:
            result.append([x for x in graph[node] if x not in forb or x.isupper()])
        return result
    else:
        forbidden = forbidden_nodes.copy()
        return [[x for x in graph[node] if x not in forbidden or x.isupper()]]


part1_solutions = set()


def get_all_paths(source, destination, graph, visited_nodes, path):
    visited_nodes.append(source)
    path.append(source)
    if source == destination:
        part1_solutions.add(','.join(path))
        return
    neighbors = get_neighbors(source, graph, visited_nodes)
    for neighbor in neighbors:
        get_all_paths(neighbor, destination, graph, visited_nodes.copy(), path.copy())


get_all_paths('start', 'end', graph, [], [])
print(len(part1_solutions))
