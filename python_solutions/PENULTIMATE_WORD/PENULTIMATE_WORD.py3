"""
Write a program which finds the next-to-last word in a string.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input
example is the following:

some line with text
another line

Each line has more than one word.

OUTPUT SAMPLE:

Print the next-to-last word in the following way:

with
another
"""
from sys import argv


def penultimate(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            words = line.rstrip().split()
            print(words[-2])


if __name__ == '__main__':
    penultimate(argv[1])
