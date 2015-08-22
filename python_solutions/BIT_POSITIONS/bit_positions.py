"""Given a number n and two integers p1,p2 determine if the bits in
position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma
separated list of 3 integers, one list per line. E.g.

86,2,3
125,1,2

OUTPUT SAMPLE:

Print to stdout, 'true'(lowercase) if the bits are the same,
else 'false'(lowercase). E.g.

true
false
"""

from sys import argv


INPUT_FILE = argv[1]


def parse_input(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            n, p1, p2 = map(int, line.split(','))
            bits(n, p1, p2)


def bits(n, p1, p2):
    binary_form = bin(n)
    # bits here are right to left
    if binary_form[-p1] == binary_form[-p2]:
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    parse_input(INPUT_FILE)
