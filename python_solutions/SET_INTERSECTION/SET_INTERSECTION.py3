'''
You are given two sorted list of numbers (ascending order). The lists themselves
are comma delimited and the two lists are semicolon delimited. Print out the
intersection of these two sets.

INPUT SAMPLE:

File containing two lists of ascending order sorted integers, comma delimited,
one per line. E.g.
1,2,3,4;4,5,6
20,21,22;45,46,47
7,8,9;8,9,10,11,12

OUTPUT SAMPLE:

Print out the ascending order sorted intersection of the two lists, one per
line. Print empty new line in case the lists have no intersection. E.g.
4

8,9
'''
from sys import argv


def main(input_file):
    """Accept formatted file, print output as described in module docs"""
    with open(input_file, mode='r') as file:
        for line in file:
            # split on the ; into two lists
            set1, set2 = split(line)
            # print set intersections of the two lists
            intersection = set1 & set2
            print(*intersection, sep=",")


def split(line):
    """Input string as described in module docstring, return 2 sets of ints."""
    set1 = {int(x) for x in (line.split(';')[0]).split(',')}
    set2 = {int(x) for x in (line.split(';')[1]).split(',')}
    return set1, set2


if __name__ == '__main__':
    main(argv[1])
