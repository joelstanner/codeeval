"""
SELF DESCRIBING NUMBERS
CHALLENGE DESCRIPTION:


A number is a self-describing number when (assuming digit positions are labeled
0 to N-1), the digit in each position is equal to the number of times that that
digit appears in the number.

INPUT SAMPLE:

The first argument is the pathname to a file which contains test data, one test
case per line. Each line contains a positive integer. E.g.

2020
22
1210

OUTPUT SAMPLE:

If the number is a self-describing number, print out 1. If not, print out 0. E.g.

1
0
1

For the curious, here's how 2020 is a self-describing number: Position '0' has
value 2 and there is two 0 in the number. Position '1' has value 0 because there
are not 1's in the number. Position '2' has value 2 and there is two 2. And the
position '3' has value 0 and there are zero 3's.
"""
from sys import argv


def main(input_file):
    with open(input_file, "r") as in_file:
        for line in in_file:
            sd_num_status = is_self_describe(line)
            print(sd_num_status)


def is_self_describe(line):
    """Check if number is self describing, return 1 if so, 0 if not."""
    num_str = line.rstrip()

    if len(num_str) <= 10:
        numlist = list(num_str)
        for x in range(len(numlist)):  # pylint: disable=invalid-name
            if int(numlist[x]) == numlist.count(str(x)):
                continue
            else:
                return 0
        return 1
    return 0


if __name__ == '__main__':
    main(argv[1])
