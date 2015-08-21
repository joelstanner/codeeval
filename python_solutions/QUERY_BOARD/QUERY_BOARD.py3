"""
There is a board (matrix). Every cell of the board contains one integer, which
is 0 initially.

The next operations can be applied to the Query Board:
SetRow i x: it means that all values in the cells on row "i" have been changed
    to value "x" after this operation.
SetCol j x: it means that all values in the cells on column "j" have been
    changed to value "x" after this operation.
QueryRow i: it means that you should output the sum of values on row "i".
QueryCol j: it means that you should output the sum of values on column "j".

The board's dimensions are 256x256
"i" and "j" are integers from 0 to 255
"x" is an integer from 0 to 31

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each
line in this file contains an operation of a query. E.g.

SetCol 32 20
SetRow 15 7
SetRow 16 31
QueryCol 32
SetCol 2 14
QueryRow 10
SetCol 14 0
QueryRow 15
SetRow 10 1
QueryCol 2

OUTPUT SAMPLE:

For each query, output the answer of the query. E.g.

5118
34
1792
3571
"""
from sys import argv


class QueryBoard:
    def __init__(self, row=256, col=256):
        self.row = row
        self.col = col

        self.board = [[0 for x in range(self.row)] for x in range(self.col)]

    def set_row(self, i, val):
        for _ in range(self.row):
            self.board[i][_] = val

    def set_col(self, j, val):
        for _ in range(self.row):
            self.board[_][j] = val

    def query_row(self, row):
        return sum(self.board[row])

    def query_col(self, col):
        temp = []
        for j in range(self.col):
            temp.append(self.board[j][col])
        return sum(temp)

    def __repr__(self):
        return str(self.board)


def main(input_file):
    query = QueryBoard()

    with open(input_file, 'r') as file:
        for line in file:
            cmd, *args = line.rstrip().split()

            if cmd == "SetRow":
                result = query.set_row(int(args[0]), int(args[1]))
            elif cmd == "SetCol":
                result = query.set_col(int(args[0]), int(args[1]))
            elif cmd == "QueryRow":
                result = query.query_row(int(args[0]))
            elif cmd == "QueryCol":
                result = query.query_col(int(args[0]))

            if result is not None:
                print(result)


if __name__ == '__main__':
    main(argv[1])
