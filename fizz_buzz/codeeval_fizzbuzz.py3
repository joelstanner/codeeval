"""Accept a text file and do the fizzbuzz upon it.

Your program should accept a file as its first argument.
The file contains multiple separated lines; each line contains
3 numbers that are space delimited. The first number is the first
divider (X), the second number is the second divider (Y), and the
third number is how far you should count (N). You may assume that
the input file is formatted correctly and the numbers are valid
positive integers.
"""

from __future__ import print_function
import sys


INPUT_FILE = sys.argv[1]


def parse_input(input_file):
    values = []

    with open(input_file, mode='r') as f:
        for line in f:
            #convert the strings to ints
            nums = [int(s) for s in line.split()]
            values.append(nums)

    return values


def fizzbuzz(X, Y, N):
    for val in range(1, N + 1):

        if val % X == 0 and val % Y == 0:
            print('FB', end='')
        elif val % X == 0:
            print('F', end='')
        elif val % Y == 0:
            print('B', end='')
        else:
            print(val, end='')

        if val == N:
            print()
        elif val < N:
            print(' ', end='')


def process():
    values = parse_input(INPUT_FILE)
    for val in values:
        X, Y, Z = val[0], val[1], val[2]
        fizzbuzz(X, Y, Z)


process()
