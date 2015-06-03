"""Given numbers x and n, where n is a power of 2, print out the
smallest multiple of n which is greater than or equal to x. Do not
use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma
separated list of two integers, one list per line. E.g.

13,8
17,16

OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or
equal to x, one per line. E.g.

16
32
"""

import sys


INPUT_FILE = sys.argv[1]


def parse_input(input_file):
    with open(input_file, mode='r') as f:
        for line in f:
            data = line.split(",")
            x = int(data[0])
            n = int(data[1])
            multiples(x, n)


def multiples(x, n):
    """x is the number in question, n is a power of 2"""
    multiple = 2
    if n >= x:
        return n
    else:
        while n * multiple < x:
            if n * multiple > x:
                print(n * multiple)
                return
            else:
                multiple += 1
        print(n * multiple)


if __name__ == '__main__':
    parse_input(INPUT_FILE)
