"""
RIGHTMOST CHAR
CHALLENGE DESCRIPTION:

You are given a string 'S' and a character 't'. Print out the position of the
rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. The
position to be printed out is zero based.

INPUT SAMPLE:

The first argument will ba a path to a filename, containing a string and a
character, comma delimited, one per line. Ignore all empty lines in the input
file. E.g.

Hello World,r
Hello CodeEval,E

OUTPUT SAMPLE:

Print out the zero based position of the character 't' in string 'S', one per
line. Do NOT print out empty lines between your output.

E.g.

8
10
"""
from sys import argv

def main(input_file):
    with open(input_file, "r") as infile:
        for line in infile:
            line = line.rstrip()
            try:
                items = line.split(",")
                rightmost_index = items[0].rfind(items[1])
                print(rightmost_index)
            except IndexError:
                continue

if __name__ == '__main__':
    main(argv[1])
