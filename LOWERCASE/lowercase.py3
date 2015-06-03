"""Given a string write a program to convert it into lowercase.

INPUT SAMPLE:

The first argument will be a path to a filename containing sentences,
one per line. You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text

OUTPUT SAMPLE:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text
"""


from sys import argv


INPUT_FILE = argv[1]


def lowercase(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            print(line.rstrip().lower())


if __name__ == '__main__':
    lowercase(INPUT_FILE)
