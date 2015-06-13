"""
Print out the sum of integers read from a file.

INPUT SAMPLE:

The first argument to the program will be a path to a filename containing
a positive integer, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print out the sum of all the integers read from the file. E.g.

17
"""

from sys import argv


INPUT_FILE = argv[1]


def sum_from_file(input_file):
    file_sum = 0
    with open(input_file, mode='r') as f:
        for line in f:
            file_sum += int(line)
    print(file_sum)


if __name__ == '__main__':
    sum_from_file(INPUT_FILE)
