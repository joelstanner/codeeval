"""
Given a sequence, write a program to detect cycles within it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename
containing a sequence of numbers (space delimited). The file can have
multiple such lines. E.g

2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3

OUTPUT SAMPLE:

Print to stdout the first cycle you find in each sequence. Ensure that
there are no trailing empty spaces on each line you print. E.g.

6 3 1
49
1 2 3

The cycle detection problem is explained more widely on wiki

Constrains:
The elements of the sequence are integers in range [0, 99]
The length of the sequence is in range [0, 50]
"""


from sys import argv


INPUT_FILE = argv[1]


def detect_cycle(input_file):
    """detect a cycle"""

    with open(input_file, mode="r") as file:
        for line in file:
            cycle_line = line.split()
            result = cycle_check(cycle_line)
            print(*result, sep=" ")


def cycle_check(cycle_line):
    """find the cycle"""
    while cycle_line:
        check1 = cycle_line.pop(0)
        if check1 in cycle_line:
            loop_point = cycle_line.index(check1)
            loop = cycle_line[:loop_point]
            loop.insert(0, check1)
            return loop


if __name__ == '__main__':
    detect_cycle(INPUT_FILE)
