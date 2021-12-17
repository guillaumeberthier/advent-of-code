#!/usr/bin/python

import sys

file_path = str(sys.argv[1])
f = open(file_path, 'r')
inputs = f.readline().split(' ')
x, y = inputs[2], inputs[3]

x = x[2:-1]
y = y[2:]

x, y = [int(i) for i in x.split('..')], [int(i) for i in y.split('..')]
x_range = range(x[0], x[1] + 1)
y_range = range(y[0], y[1] + 1)


def step(x, y, x_vel, y_vel):
    return (x + x_vel, y + y_vel), (max(x_vel-1, 0), y_vel - 1)


highests = []
possibles = set()


def compute(x_vel, y_vel, x_range, y_range):
    while True:
        start = 0, 0
        vel = (x_vel, y_vel)
        highest = 0
        while start[0] <= list(x_range)[-1] and start[1] >= list(y_range)[0]:
            start, vel = step(start[0], start[1], vel[0], vel[1])
            if highest < start[1]:
                highest = start[1]
            if start[0] in list(x_range) and start[1] in list(y_range):
                highests.append(highest)
                possibles.add((x_vel, y_vel))
        return


for x_vel in range(0, 400):
    for y_vel in range(-400, 400):
        compute(x_vel, y_vel, x_range, y_range)
print(max(highests))
print(len(possibles))
