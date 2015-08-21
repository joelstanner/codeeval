"""Write a program which prints all the permutations of a string in
alphabetical order. We consider that digits < upper case letters <
lower case letters. The sorting should be performed in ascending order.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file
contains input strings, one per line.

For example:

hat
abc
Zu6

OUTPUT SAMPLE:

Print to stdout the permutations of the string separated by comma, in
alphabetical order.

For example:

aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6
"""

import sys
from itertools import permutations


INPUT_FILE = sys.argv[1]


def parse_input(input_file):
    with open(input_file, mode='r') as f:
        for line in f:
            do_permutations(line)


def do_permutations(line):
    data = permutations(sorted(line.strip()))
    last = next(data)
    for val in data:
        print("".join(last), end=",")
        last = val
    print("".join(last))


if __name__ == '__main__':
    parse_input(INPUT_FILE)
