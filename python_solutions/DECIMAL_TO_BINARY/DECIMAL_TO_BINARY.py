"""
You are given a decimal (base 10) number, print its binary representation.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename
containing decimal numbers greater or equal to 0, one per line.

Ignore all empty lines.

For example:

2
10
67

OUTPUT SAMPLE:

Print the binary representation, one per line.

For example:

10
1010
1000011
"""
from sys import argv


def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            num = int(line.rstrip())
            print(bin(num)[2:])


if __name__ == '__main__':
    main(argv[1])
