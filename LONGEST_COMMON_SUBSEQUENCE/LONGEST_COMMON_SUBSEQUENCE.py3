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
import re


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


def make_char_dict(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = (m.start for m in re.finditer(char, string))
    return char_dict


def main(input_file):
    with open(input_file, "r") as file:
        # split strings on the semi-colon
        for line in file:
            string1, string2 = line.rstrip().split(';')

            # determine common letters using a set
            string_set = set(string1) & set(string2)

            # make new strings with only common letters in order
            string1_redux = new_string_from_set(string_set, string1)
            string2_redux = new_string_from_set(string_set, string2)

            # create dictionary with index pos of each char in
            # string as a generator
            string1_char_positions = make_char_dict(string1_redux)
            string2_char_positions = make_char_dict(string2_redux)

            # build the max len
            max_string = build_max(
                string1_redux, string2_redux, string1_char_positions,
                string2_char_positions)

            print(max_string)


if __name__ == '__main__':
    main(argv[1])
