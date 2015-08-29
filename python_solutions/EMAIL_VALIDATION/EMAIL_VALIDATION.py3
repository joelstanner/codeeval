"""
You are given several strings that may/may not be valid emails. You should
write a regular expression that determines if the email id is a valid email
id or not. You may assume all characters are from the english language.

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will
contain several text strings, one per line. Ignore all empty lines. E.g

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com

OUTPUT SAMPLE:

Print out 'true' (all lowercase) if the string is a valid email. Else print out
'false' (all lowercase). E.g.

true
false
false
true
"""
from sys import argv
import re


def parse_input(string):
    """Return true if email is valid, else false."""
    string = string.rstrip()
    match = re.search(r'(\S+)(?=@)@((?!@)(\S+)[.][a-zA-Z]+)', string)

    if match is not None:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    with open(argv[1], 'r') as file:
        for line in file:
            parse_input(line)
