"""
You have coordinates of 2 points and need to find the distance between them.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input
example is the following


(25, 4) (1, -6)
(47, 43) (-25, -11)

All numbers in input are integers between -100 and 100.

OUTPUT SAMPLE:

Print results in the following way.

26
90
You don't need to round the results you receive. They must be integer numbers.
"""
from sys import argv


def dist(a, b):
    """Use pythagorean theorem to find the distance"""
    return (a ** 2 + b ** 2) ** (1 / 2)


def parse_input(string):
    """Return x and y distances as ints from '(x1, y1) (x2, y2)'."""
    string = string.translate({ord(i): None for i in '(),'})
    x1, y1, x2, y2 = [int(x) for x in string.split()]
    return x1 - x2, y1 - y2


def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            a, b = parse_input(line)
            print(int(dist(a, b)))

if __name__ == '__main__':
    main(argv[1])
