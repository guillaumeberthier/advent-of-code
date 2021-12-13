#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
dots, folds = f.read().split('\n\n')

dots = dots.splitlines()
dots = [x.split(',') for x in dots]
dots = set([(int(x[0]), int(x[1])) for x in dots])

folds = [x.split(' ')[2].split('=') for x in folds.splitlines()]


def get_min_x(dots):
    return min([x[0] for x in dots])


def get_min_y(dots):
    return min([x[1] for x in dots])


def get_max_x(dots):
    return max([x[0] for x in dots])


def get_max_y(dots):
    return max([x[1] for x in dots])


def fold_x(x, dots):
    new_dots = set()
    for dot in dots:
        if dot[0] > x:
            new_x = x - (dot[0] - x)
            new_dots.add((new_x, dot[1]))
        else:
            new_dots.add(dot)
    min_x = get_min_x(new_dots)
    if min_x < 0:
        new_dots = [(x[0] + (-1 * min_x), x[1]) for x in new_dots]
    return new_dots


def fold_y(y, dots):
    new_dots = set()
    for dot in dots:
        if dot[1] > y:
            new_y = y - (dot[1] - y)
            new_dots.add((dot[0], new_y))
        else:
            new_dots.add(dot)
    min_y = get_min_y(new_dots)
    if min_y < 0:
        new_dots = [(x[0], x[1] + (-1 * min_y)) for x in new_dots]
    return new_dots


def fold(axis, value, dots):
    if axis == 'x':
        return fold_x(value, dots)
    else:
        return fold_y(value, dots)


def print_board(dots):
    min_x, min_y = get_min_x(dots), get_min_y(dots)
    max_x, max_y = get_max_x(dots), get_max_y(dots)
    board = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for dot in dots:
        board[dot[1] + min_y][dot[0] + min_x] = '#'
    for row in board:
        print(''.join(row))


# Part 1
print(len(fold(folds[0][0], int(folds[0][1]), dots)))

# Part 2
next_dots = dots.copy()
for pli in folds:
    next_dots = fold(pli[0], int(pli[1]), next_dots)
print_board(next_dots)
