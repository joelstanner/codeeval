"""
LONGEST COMMON SUBSEQUENCE

CHALLENGE DESCRIPTION:

You are given two sequences. Write a program to determine the longest common
subsequence between the two strings (each string can have a maximum length of
50 characters). NOTE: This subsequence need not be contiguous. The input file
may contain empty lines, these need to be ignored.

INPUT SAMPLE:

The first argument will be a path to a filename that contains two strings per
line, semicolon delimited. You can assume that there is only one unique
subsequence per test case. E.g.

XMJYAUZ;MZJAWXU

OUTPUT SAMPLE:

The longest common subsequence. Ensure that there are no trailing empty spaces
on each line you print. E.g.

MJAU
"""
from sys import argv


def main(input_file):
    with open(input_file, "r") as file:
        # split strings on the semi-colon
        # determine common letters using a set
        # make new strings with only common letters in order
        # create dictionary with index pos of each char in 2nd string

        pass
