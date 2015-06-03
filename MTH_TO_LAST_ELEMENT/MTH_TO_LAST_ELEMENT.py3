"""Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space
delimited characters followed by an integer. The integer represents an index
in the list (1-based), one per line.

For example:

a b c d 4
e f g h 2

OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the
index is larger than the number of elements in the list, ignore that input.

For example:

a
g
"""
from __future__ import print_function
import sys


INPUT_FILE = sys.argv[1]


def parse_input(input_file):
    """Split line into a list, then process."""
    with open(input_file, mode='r') as f:
        for line in f:
            data = line.split()
            mth_to_last(data)


def mth_to_last(data):
    """Check if index number is valid, then process.

    The index number is the last item in the list. If the list is
    shorter than the index number, return. Otherwise print the item
    in the list that corresponds to the index number, going backwards.
    We need to add a -1 because the index number takes up one index in
    the list.
    """
    index_num = int(data[-1])
    if len(data) < index_num or index_num < 1:
        return
    print(data[-index_num - 1])


if __name__ == '__main__':
    parse_input(INPUT_FILE)
