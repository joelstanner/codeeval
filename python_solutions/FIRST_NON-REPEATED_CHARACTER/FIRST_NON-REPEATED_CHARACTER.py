"""
Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains strings.

For example:

yellow
tooth

OUTPUT SAMPLE:

Print to stdout the first non-repeated character, one per line.

For example:

y
h
"""
from sys import argv
from collections import defaultdict


def parse_input(input_file):
    """Send each line in a file to the non_repeat function"""
    with open(input_file, mode="r") as file:
        for line in file:
            info = line.rstrip()
            result = non_repeat(info)
            print(result)


def non_repeat(string):
    """Create a defaultdict, return the first character with a val of 1"""
    char_count = defaultdict(int)

    for char in string:
        char_count[char] += 1

    for char in string:
        if char_count[char] == 1:
            return char
        else:
            continue


if __name__ == '__main__':
    parse_input(argv[1])
