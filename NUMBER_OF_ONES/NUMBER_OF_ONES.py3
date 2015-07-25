"""
Write a program which determines the number of 1 bits in the internal
representation of a given integer.

INPUT SAMPLE:

The first argument is a path to a file. The file contains integers,
one per line.

For example:

10
22
56

OUTPUT SAMPLE:

Print to stdout the number of ones in the binary form of each number.

For example:

2
3
3
"""
from sys import argv


def main(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            bin_rep = bin(int(line.rstrip()))
            print(bin_rep.count('1'))

if __name__ == '__main__':
    main(argv[1])
