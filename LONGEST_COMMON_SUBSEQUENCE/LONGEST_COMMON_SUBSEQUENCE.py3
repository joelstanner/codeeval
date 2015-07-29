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


def new_string_from_set(string_set, string):
    """Return a string with only characters in the set."""
    for char in string:
        if char not in string_set:
            string = string.replace(char, "")

    return string


def build_max(string1_redux, string2_redux):
    str_pos1 = 0
    str_pos2 = 0
    temp_str = ""
    max_string = ""

    char = string1_redux[str_pos1]
    str_pos2 = string2_redux.index(char)

    # chop off letters prior to found char.
    temp_str = string2_redux[str_pos2:]

    # Keep max len string until a longer one is found.
    max_string += char

    # next char is string2_redux's next
    str_pos1 = # next str1 index pos of str2 next char - from list

    # iterate next char, drop chars in 2nd until next char found

    # Perhaps do it again by dropping 1st string chars
    #     - might make a difference

def main(input_file):
    with open(input_file, "r") as file:
        # split strings on the semi-colon
        # determine common letters using a set
        # make new strings with only common letters in order
        # create dictionary with index pos of each char in 2nd string

        pass
