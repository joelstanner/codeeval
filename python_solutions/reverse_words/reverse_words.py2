"""Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences,
one per line. Empty lines are also possible.

    Hello World
    Hello CodeEval


OUTPUT SAMPLE:

Print to stdout each sentence with the reversed words in it,
one per line. Empty lines in the input should be ignored.
Ensure that there are no trailing empty spaces in each line you print.

For example:
    World Hello
    CodeEval Hello
"""

from __future__ import print_function
import sys


INPUT_FILE = sys.argv[1]


def read_file(input_file):
    lines = []
    with open(input_file, mode='r') as f:
        for line in f:
            # check if line is empty first
            if line.strip():
                lines.append(line)
            else:
                continue

    return lines


def output_lines():
    lines = read_file(INPUT_FILE)

    for line in lines:
        reverse_line = line.split()[::-1]
        print(' '.join(reverse_line))


output_lines()
