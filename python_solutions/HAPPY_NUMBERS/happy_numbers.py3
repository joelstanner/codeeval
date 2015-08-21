"""
A happy number is defined by the following process. Starting with any positive
integer, replace the number by the sum of the squares of its digits, and repeat
the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this
process ends in 1 are happy numbers, while those that do not end in 1 are
unhappy numbers.

INPUT SAMPLE:

The first argument is the pathname to a file which contains test data,
one test case per line. Each line contains a positive integer. E.g.

7
22

OUTPUT SAMPLE:

If the number is a happy number, print out 1. If not, print out 0. E.g

1
1
0

For the curious, here's why 7 is a happy number: 7->49->97->130->10->1.
Here's why 22 is NOT a happy number:
22->8->64->52->29->85->89->145->42->20->4->16->37->58->89 ...
"""

import sys

def parse_input(input_file):
    with open(input_file, mode="r") as file:
        for line in file:
            happiness(line.rstrip())


def happiness(num):
    """Return 1 if number is happy, 0 if not

    num is a string and is converted into single digit integers
    """
    happys = [int(j) for j in num]
    last = 0
    for digit in happys:
        last += digit ** 2

    if last == 1:
        print(1)
    elif last == 89:  # all unhappy numbers become 89 at some point
        print(0)
        return
    else:
        happiness(str(last))


if __name__ == '__main__':
    INPUT_FILE = sys.argv[1]
    parse_input(INPUT_FILE)
