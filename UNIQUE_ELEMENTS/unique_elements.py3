"""
You are given a sorted list of numbers with duplicates. Print out the sorted
list with duplicates removed.

INPUT SAMPLE:

File containing a list of sorted integers, comma delimited, one per line. E.g.

1,1,1,2,2,3,3,4,4
2,3,4,5,5

OUTPUT SAMPLE:

Print out the sorted list with duplicates removed, one per line.
E.g.


1,2,3,4
2,3,4,5
"""

from sys import argv

INPUT_FILE = argv[1]


def unique_elements(input_file):
    """Print out the sorted list with duplicates removed, one per line"""
    with open(input_file, mode="r") as file:
        for line in file:
            # Create a new, unique list that is a set from orig list.
            u_list = sorted(list(set([int(x) for x in line.split(',')])))
            print(*u_list, sep=",")


if __name__ == '__main__':
    unique_elements(INPUT_FILE)
