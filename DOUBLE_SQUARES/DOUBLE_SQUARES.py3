"""
A double-square number is an integer X which can be expressed as the sum of two
perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2.
Your task in this problem is, given X, determine the number of ways in which
it can be written as the sum of two squares.

For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as
being different). On the other hand, 25 can be written as 5^2 + 0^2 or as
4^2 + 3^2.
NOTE: Do NOT attempt a brute force approach. It will not work. The following
constraints hold:
0 <= X <= 2147483647
1 <= N <= 100

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
You should first read an integer N, the number of test cases. The next N
lines will contain N values of X.

5
10
25
3
0
1

OUTPUT SAMPLE:

E.g.

1
2
0
1
1
"""
from sys import argv
import math


def main(input_file):
    """Print a count of double squares for each number in a text file

    As described in the module docs.
    """
    with open(input_file, 'r') as file:
        # not currently used, but part of challenge:
        _ = int(file.readline().rstrip())
        for line in file:
            count = doublesquare(int(line.rstrip()))
            print(count)


def doublesquare(number):
    """Determines how many double squares a number has.
    From http://articles.leetcode.com/2011/01/double-square-problem-analysis.html
    Consider that:
    M = x2 + y2,
    and we have y2 = M – x2.

    We can easily tell if (M - x2) is a perfect square by taking the square
    root of it and compare it to its truncated value (deleting its fractional
    part). If both are equal, then it must be a perfect square, or else it is
    not.

    number mod 4 == 3 means it is impossible to be a sum of 2 squares. We
    check this here to save time.

    Args:
        number: An integer 0 <= number <= 2147483647

    Returns:
        A count of how many double squares the number can be represented by.
    """
    count = 0
    if not number % 4 == 3:
        # largest num we need to check
        upper = math.sqrt(number / 2)
        for i in range(0, int(upper) + 1):
            j = math.sqrt(number - i * i)
            if j == int(j):
                count += 1

    return count

if __name__ == '__main__':
    main(argv[1])
