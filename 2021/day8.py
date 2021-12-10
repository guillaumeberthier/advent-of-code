#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
rows = f.read().splitlines()

# Part 1
digits = []
for row in rows:
    outputs = row.split(' | ')[1]
    digits.extend(outputs.split(' '))

len_candidates = [2, 4, 3, 7]
sum = 0
for digit in digits:
    if len(digit) in len_candidates:
        sum += 1
print(sum)

# Part 2
digits_map = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}


def letter_count(letter, digits):
    return len(list(filter(lambda x: letter in x, digits)))


def get_c_f(letters, digits):
    if letter_count(letters[0], digits) == 8:
        return letters[0], letters[1]
    else:
        return letters[1], letters[0]


def get_a(letters, c_f_letters):
    return [x for x in letters if x not in c_f_letters][0]


def get_b_d(letters, c_f_letters, digits):
    b_d_letters = [x for x in letters if x not in c_f_letters]
    if letter_count(b_d_letters[0], digits) == 6:
        return b_d_letters[0], b_d_letters[1]
    else:
        return b_d_letters[1], b_d_letters[0]


def get_e_g(deducted_letters, digits):
    all = 'abcdefg'
    e_g_letters = [x for x in all if x not in deducted_letters]
    if letter_count(e_g_letters[0], digits) == 4:
        return e_g_letters[0], e_g_letters[1]
    else:
        return e_g_letters[1], e_g_letters[0]


sum = 0
for row in rows:
    current_map = {}
    rules, outputs = row.split(' | ')
    rules = rules.split(' ')
    outputs = outputs.split(' ')
    two = list(filter(lambda x: len(x) == 2, rules))[0]
    c, f = get_c_f(two, rules)
    current_map[c] = 'c'
    current_map[f] = 'f'
    three = list(filter(lambda x: len(x) == 3, rules))[0]
    a = get_a(three, [c, f])
    current_map[a] = 'a'
    four = list(filter(lambda x: len(x) == 4, rules))[0]
    b, d = get_b_d(four, [c, f], rules)
    current_map[b] = 'b'
    current_map[d] = 'd'
    e, g, = get_e_g([a, b, c, d, f], rules)
    current_map[e] = 'e'
    current_map[g] = 'g'

    number = ''
    for output in outputs:
        transform_output = ''.join(list(sorted([current_map[x] for x in output])))
        decipher_output = digits_map[transform_output]
        number += str(decipher_output)
    sum += int(number)
print(sum)
