#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
content = f.read()
section = content.split('\n\n')
bingo, boards_desc = section[0], section[1:]

entry_histogram = [[] for _ in range(100)]
boards = []
shadow_boards = []
for i, board in enumerate(boards_desc):
    rows = [[int(x.strip()) for x in row.split()] for row in board.splitlines()]
    for y, row in enumerate(rows):
        for x, entry in enumerate(row):
            entry_histogram[entry].append((i, x, y))
    boards.append(rows)
    shadow_boards.append([[0 for _ in range(5)] for _ in range(5)])


def winner(boards, winners):
    for i, board in enumerate(boards[:]):
        if i in winners:
            continue
        for row in board:
            if sum(row) == 5:
                print(board, winners)
                return i
        for col in list(zip(*board)):
            if sum(col) == 5:
                print(board, winners)
                return i
    return -1


def score(current, board, shadow_board):
    print(board, shadow_board)
    score_board = [[y[0] * y[1] for y in zip(x[0], x[1])] for x in zip(board, shadow_board)]
    s = sum([sum(x) for x in board]) - sum([sum(x) for x in score_board])
    return current * s


def compute_first(bingo):
    for cur_entry in bingo:
        for (i, x, y) in entry_histogram[cur_entry]:
            shadow_boards[i][y][x] = 1
        winner_index = winner(shadow_boards)
        if winner_index != -1:
            return score(cur_entry, boards[winner_index], shadow_boards[winner_index])


def compute_last(bingo):
    winners_index = []
    winners = set()
    for cur_entry in bingo:
        for (i, x, y) in entry_histogram[cur_entry]:
            if i in winners:
                continue
            shadow_boards[i][y][x] = 1
        winner_index = winner(shadow_boards, winners)
        if winner_index != -1 and winner_index not in winners:
            winners_index.append((winner_index, cur_entry))
            winners.add(winner_index)
    last_index, last_entry = winners_index.pop()
    print(last_index, last_entry)
    return score(last_entry, boards[last_index], shadow_boards[last_index])


bingo = [int(x) for x in bingo.split(',')]
#print(compute_first(bingo))
print(compute_last(bingo))
