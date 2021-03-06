"""
You are given a sorted array of positive integers and a number 'X'. Print out
all pairs of numbers whose sum is equal to X. Print out only unique pairs and
the pairs should be in ascending order

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will
contain a comma separated list of sorted numbers and then the sum 'X',
separated by semicolon. Ignore all empty lines. If no pair exists, print the
string NULL e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50

OUTPUT SAMPLE:

Print out the pairs of numbers that equal to the sum X. The pairs should
themselves be printed in sorted order i.e the first number of each pair should
be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL
"""
from sys import argv


def number_pairs(num_list, minuend):
    """Return a list of number pairs that sum to the minuend.

    This is accomplished by iterating a list of integers and
    subtracting the number from the minuend. If the difference from
    that operation is also in our list of numbers, then we have a pair.
    Remove the second number (diff) from the list so we don't duplicate.

    Args:
        num_list: A sorted list of integers.
        minuend: The number we are looking to find sums of in our num_list.

    Returns:
        A list of tuples that sum to the minuend.
    """
    pairs = []
    for subtrahend in num_list:
        diff = minuend - subtrahend
        if diff in num_list:
            pairs.append((subtrahend, diff))
            num_list.remove(diff)
    return pairs


def parse_line(line):
    """Returns a list of ints and a minuend integer.

    The line needs to be in the form '1,2,3,...;5' as described in the module
    docstring
    """
    num_list, minuend = line.split(';')
    num_list = [int(num) for num in num_list.split(',')]
    minuend = int(minuend)
    return num_list, minuend


def parse_output(output_list):
    """Return a string formed like so: '1,4;2,3'"""
    output = []
    for pair in output_list:
        temp = ",".join([str(num) for num in pair])
        output.append(temp)
    return ";".join(output)


def main(input_file):
    """Iterate the lines of a text file and print the results."""
    with open(input_file, 'r') as file:
        for line in file:
            num_list, minuend = parse_line(line)
            pairs = number_pairs(num_list, minuend)
            out_line = parse_output(pairs)
            if not out_line == '':
                print(out_line)
            else:
                print('NULL')

if __name__ == '__main__':
    main(argv[1])
