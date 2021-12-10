#!/usr/bin/python

import sys
from collections import deque
import math

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()
open = ['(', '{', '[', '<']
close_to_open = {')': '(', '}': '{', ']': '[', '>': '<'}
close_to_score = {')': 3, '}': 1197, ']': 57, '>': 25137}


# Part 1
def get_chunks_invalid_score(chunks):
    stack_chunk = deque()
    for item in chunks:
        if item in open:
            stack_chunk.append(item)
        else:
            last = stack_chunk.pop()
            if last != close_to_open[item]:
                return close_to_score[item]
    return 0


total_score = 0
for row in rows:
    chunks = [x for x in row]
    total_score += get_chunks_invalid_score(chunks)
print(total_score)

# Part 2
open_to_close = {'(': ')', '{': '}', '[': ']', '<': '>'}
close_to_score_2 = {')': 1, '}': 3, ']': 2, '>': 4}


def get_completion_score(chunks):
    stack_chunk = deque()
    for item in chunks:
        if item in open:
            stack_chunk.append(item)
        else:
            last = stack_chunk.pop()
            if last != close_to_open[item]:
                return 0

    score = 0
    while len(stack_chunk) > 0:
        last = stack_chunk.pop()
        last_close = open_to_close[last]
        last_score = close_to_score_2[last_close]
        score *= 5
        score += last_score
    return score


scores = []
for row in rows:
    chunks = [x for x in row]
    scores.append(get_completion_score(chunks))
scores = sorted(list(filter(lambda x: x != 0, scores)))
print(scores[math.floor(len(scores)/2)])
