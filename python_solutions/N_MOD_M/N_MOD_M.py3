"""
Given two integers N and M, calculate N Mod M (without using any inbuilt
modulus operator).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Each line in this file contains two comma separated positive integers. E.g.

20,6
2,3

You may assume M will never be zero.

OUTPUT SAMPLE:

Print out the value of N Mod M
"""
from sys import argv


def main(infile):
    """Accept a text file and perform N % M on each line of ints"""
    with open(infile, 'r') as file:
        for line in file:
            ints = [int(x) for x in line.rstrip().split(',')]
            div = ints[0] // ints[1]
            mod = ints[0] - ints[1] * div
            print(mod)

if __name__ == '__main__':
    main(argv[1])
