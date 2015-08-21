"""
TRAILING STRING
CHALLENGE DESCRIPTION:


There are two strings: A and B. Print 1 if string B occurs at the end of string
A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two
comma-delimited strings, one per line. Ignore all empty lines in the input
file.

For example:

Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose
OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise,
print 0.

For example:

1
1
0
"""
from sys import argv


def main(input_file):
    """Input a text file, iterate over the lines, return 1 or 0.

    Each line compares the last string to the right of the comma
    with the end of the string to the left of the comma.

    Args:
        input_file: a path to the input filename containing two
        comma-delimited strings, one per line.

    Prints:
        1 if the second string occurs at the end of the first string.
        Otherwise, print 0.
    """
    with open(input_file, "r") as file:
        for line in file:
            string = line.rstrip()
            try:
                str1, str2 = string.split(',')
                ends = str1.endswith(str2)
                print(1 if ends else 0)
            except ValueError:
                continue


if __name__ == '__main__':
    main(argv[1])
