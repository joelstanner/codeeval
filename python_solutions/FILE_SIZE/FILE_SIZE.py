"""
FILE SIZE
CHALLENGE DESCRIPTION:


Print the size of a file in bytes.

INPUT:

The first argument to your program has the path to the file you need to
check the size of.

OUTPUT SAMPLE:

Print the size of the file in bytes. E.g.

55
"""

from sys import argv
import os

INPUT_FILE = argv[1]


def file_size(input_file):
    statinfo = os.stat(input_file)
    print(statinfo.st_size)


if __name__ == '__main__':
    file_size(INPUT_FILE)
