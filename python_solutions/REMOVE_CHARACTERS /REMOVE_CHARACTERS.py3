"""Write a program which removes specific characters from a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the source strings
and the characters that need to be scrubbed. Each source string and characters
you need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def

OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. Ensure that there are no
trailing empty spaces on each line you print.

For example:

how re you
hllo worl
"""
import sys


INPUT_FILE = sys.argv[1]


def strip_chars(input_file):
    """Read a line, strip the chars, print new line.

    We split the line at the comma so that we have a list with
    the first item being the string and the second the characters
    we need to strip. Map the ordnial numbers of strip characters
    to None. Use the translate string method to remap any characters
    in our string to None.
    """
    with open(input_file, mode='r') as f:
        for line in f:
            data = line.split(",")

            #create dictionary to map ordinal numbers to None
            #remove whitespaces first.
            trans_table = dict.fromkeys(map(ord, data[1].strip()), None)
            print(data[0].translate(trans_table))

if __name__ == '__main__':
    strip_chars(INPUT_FILE)
