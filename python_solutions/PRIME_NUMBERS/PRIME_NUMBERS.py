"""
PRIME NUMBERS
CHALLENGE DESCRIPTION:

Print out the prime numbers less than a given number N. For bonus points your
solution should run in N*(log(N)) time or better. You may assume that N is
always a positive integer.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain an integer
n < 4,294,967,295. E.g.

10
20
100

OUTPUT SAMPLE:

For each line of input, print out the prime numbers less than N, in ascending
order, comma delimited. (There should not be any spaces between the comma and
numbers) E.g.

2,3,5,7
2,3,5,7,11,13,17,19
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
"""
from sys import argv
from math import sqrt
from itertools import count, islice
import bisect

PRIMES_LIST = [2, 3]


def is_prime(number):
    """Return True if a nuber is prime"""
    if number < 2:
        return False
    elif number in PRIMES_LIST:
        return True
    return all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


def make_primes_list(number):
    """Make a list of primes less than number.

    Only add primes that are not currently in the list
    """
    for num in range(PRIMES_LIST[-1] + 2, number, 2):
        if is_prime(num):
            PRIMES_LIST.append(num)


def print_primes(number):
    """Print a list of primes that are less than the number as per challenge"""
    idx = bisect.bisect(PRIMES_LIST, number)
    print(*PRIMES_LIST[:idx], sep=",")


if __name__ == '__main__':
    with open(argv[1], 'r') as file:
        for line in file:
            if int(line) > 4294967294:
                print("Number is too big")
            elif int(line) <= PRIMES_LIST[-1]:
                print_primes(int(line))
            elif int(line) > PRIMES_LIST[-1]:
                make_primes_list(int(line))
                print_primes(int(line))
