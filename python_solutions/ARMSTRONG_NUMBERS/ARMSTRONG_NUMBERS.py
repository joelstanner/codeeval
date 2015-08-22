"""
An Armstrong number is an n-digit number that is equal to the sum of the n'th
powers of its digits. Determine if the input numbers are Armstrong numbers.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each
line in this file has a positive integer. E.g.

6
153
351

OUTPUT SAMPLE:

Print out True/False if the number is an Armstrong number or not. E.g.

True
True
False
"""
from sys import argv


def armstrong_number(number):
    """Compute and return the armstrong number"""
    total = 0
    num_len = len(number)
    for i in range(len(number)):
        total += int(number[i]) ** num_len
    return total


def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            num = line.rstrip()
            arm_num = armstrong_number(num)
            if (arm_num) == int(num):
                print(True)
            else:
                print(False)


if __name__ == '__main__':
    main(argv[1])
