"""
Write a program which checks input numbers and determines whether a number is
even or not.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input
example is the following

701
4123
2936

OUTPUT SAMPLE:

Print 1 if the number is even or 0 if the number is odd.

0
0
1
All numbers in input are integers > 0 and < 5000.
"""
from sys import argv


def check_even(num):
    if num % 2 == 0:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    with open(argv[1], 'r') as file:
        for line in file:
            check_even(int(line.rstrip()))
