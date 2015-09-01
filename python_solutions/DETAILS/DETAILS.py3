"""
There are two details on a M*N checkered field. The detail X
covers several (at least one first cell) cells in each line. The
detail Y covers several (at least one last cell) cells. Each cell
is either fully covered with a detail or not.

For example:

Also, the details may have cavities (or other complex
structures).

The detail Y starts moving left (without any turn) until it bumps
into the X detail at least with one cell. Determine by how many
cells the detail Y will be moved.

INPUT SAMPLE:

The first argument is a file with different test cases. Each test
case contains a matrix the lines of which are separated by comma.
(Empty cells are marked as ".")

For example:

XX.YY,
XXX.Y,
X..YY,
XX..Y

XXX.YYYY,
X...Y..Y,
XX..YYYY,
X.....YY,
XX....YY

XX...YY,X....YY,XX..YYY,X..YYYY
XXYY,X..Y,XX.Y

OUTPUT SAMPLE:

Print out the number of cells the detail Y will be moved.

For example:

1
1
2
0
CONSTRAINTS:

The matrices can be of different M*N sizes. (2 <= M <= 10, 2 <= N <= 10)
Number of test cases is 40.
"""
from sys import argv


def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            result = get_details(line.rstrip())
            print(result)


def get_details(line):
    empty = None
    empty_min = 10

    for detail in line.split(','):
        y_pos = detail.find('Y')
        empty = detail.count('.', 0, y_pos)
        if empty < empty_min:
            empty_min = empty
    return empty_min

if __name__ == '__main__':
    main(argv[1])