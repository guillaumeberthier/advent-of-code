#!/usr/bin/python
import sys

file_path = str(sys.argv[1])
gamma_rate = ''
epsilon_rate = ''

f = open(file_path, 'r')
content = f.read()
diagnostic_report = content.splitlines()

for x in range(len(diagnostic_report[0])):
    zeros = 0
    ones = 0
    for y in range(len(diagnostic_report)):
        if diagnostic_report[y][x] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'
    else:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# oxygen
ox_diagnostic_report = diagnostic_report[:]
while len(ox_diagnostic_report) > 1:
    for i in range(len(diagnostic_report[0])):
        if len(ox_diagnostic_report) == 1:
            break
        zeros = 0
        ones = 0
        for entry in ox_diagnostic_report[:]:
            if entry[i] == '0':
                zeros += 1
            else:
                ones += 1
        max = '1' if ones >= zeros else '0'
        ox_diagnostic_report = list(filter(lambda x: (x[i] == max), ox_diagnostic_report[:]))

# cO2
co2_diagnostic_report = diagnostic_report[:]
while len(co2_diagnostic_report) > 1:
    for i in range(len(diagnostic_report[0])):
        if len(co2_diagnostic_report) == 1:
            break
        zeros = 0
        ones = 0
        for entry in co2_diagnostic_report[:]:
            if entry[i] == '0':
                zeros += 1
            else:
                ones += 1
        max = '1' if ones < zeros else '0'
        co2_diagnostic_report = list(filter(lambda x: (x[i] == max), co2_diagnostic_report[:]))

print(int(ox_diagnostic_report[0], 2) * int(co2_diagnostic_report[0], 2))

#Codehorrible