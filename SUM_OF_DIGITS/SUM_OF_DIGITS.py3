"""Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers,
one per line. E.g.

23
496

OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer,
one per line. E.g.

5
19
"""

from sys import argv


INPUT_FILE = argv[1]


def sum_of_digits(digits):
    with open(digits, 'r') as f:
        for line in f:
            digi_sum = 0
            for char in line.strip():
                digi_sum += int(char)
            print(digi_sum)
    

if __name__ == '__main__':
    sum_of_digits(INPUT_FILE)
