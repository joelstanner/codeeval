"""
The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2)
when n>1. Given an integer n≥0, print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing integer numbers,
one per line. E.g.

5
12

OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144
"""

from sys import argv


INPUT_FILE = argv[1]


def memo(func):
    cache = {}

    def memf(*x):
        if x not in cache:
            cache[x] = func(*x)
        return cache[x]
    return memf

@memo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            print(fibonacci(int(line.rstrip())))
