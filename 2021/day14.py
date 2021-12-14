#!/usr/bin/python

import sys


def add_element(element, map, count):
    if element in map:
        map[element] += count
    else:
        map[element] = count


def step(couple_count, letter_count):
    next_couple_count = {}
    next_letter_count = letter_count.copy()
    for couple in couple_count:
        count = couple_count[couple]
        new_letter = reactions_map[couple]
        add_element(couple[0] + new_letter, next_couple_count, count)
        add_element(new_letter + couple[1], next_couple_count, count)
        add_element(new_letter, next_letter_count, count)
    return next_couple_count, next_letter_count


def get_result(couple_count, letter_count, n):
    next_couple_count, next_letter_count = couple_count.copy(), letter_count.copy()
    for i in range(n):
        next_couple_count, next_letter_count = step(next_couple_count, next_letter_count)
    max_key = max(next_letter_count, key=next_letter_count.get)
    min_key = min(next_letter_count, key=next_letter_count.get)
    return next_letter_count[max_key] - next_letter_count[min_key]


file_path = str(sys.argv[1])
f = open(file_path, 'r')
template, reactions = f.read().split('\n\n')
reactions = reactions.splitlines()
reactions_map = {}
couple_count = {}
letter_count = {}
for reaction in reactions:
    left, right = reaction.split(' -> ')
    reactions_map[left] = right

for i in range(1, len(template)):
    window = template[i-1:i+1]
    add_element(window, couple_count, 1)
    add_element(window[0], letter_count, 1)
add_element(template[-1], letter_count, 1)

print(get_result(couple_count, letter_count, 10))
print(get_result(couple_count, letter_count, 40))
