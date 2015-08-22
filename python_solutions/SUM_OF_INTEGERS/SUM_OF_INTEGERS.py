"""
Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:

The first argument is a path to a filename containing a comma-separated list of
integers, one per line.

For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10

OUTPUT SAMPLE:

Print to stdout the largest sum. In other words, of all the possible contiguous
subarrays for a given array, find the one with the largest sum, and print that
sum.

For example:

8
12
"""
from sys import argv


def main(infile):
    """Print the max sum of each line in the input file"""
    with open(infile, 'r') as file:
        for line in file:
            int_list = [int(x) for x in line.rstrip().split(',')]
            print(largest_sum(int_list))


def largest_sum(int_list):
    """Return the maximum sum of of all the possible contiguous subarrays.

    Input is an array of integers. All possible summations of contiguous
    subarrays are calulated and the maximum is updated whenever a sum is
    greater than the current maximum.

    Args:
        int_list: A list of integers

    Returns:
        max_sum: An integer that is the maximum sum found.
    """
    max_sum = float("-inf")
    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list) + 1):
            current_sum = sum(int_list[i:j])
            # print(int_list[i:j])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


if __name__ == '__main__':
    main(argv[1])
