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


def _clear_dicts(string1_char_positions, string1_redux,
                 string2_char_positions, string2_redux):
    string1_char_positions.clear()
    string2_char_positions.clear()
    string1_char_positions = make_char_dict(string1_redux)
    string2_char_positions = make_char_dict(string2_redux)
    return string1_char_positions, string2_char_positions


def build_max(string1_redux, string2_redux,
              string1_char_positions, string2_char_positions):
    str1_pointer = 0
    str1_temp_pointer = 0
    str2_pointer = 0
    temp_pointer = 0
    temp_str = ""
    max_string = ""
    temp_max_str = ""
    ultimate_max = min(len(string1_redux), len(string2_redux))
    cycles = 0

    while (len(max_string) <= ultimate_max and
           len(max_string) < ultimate_max - str1_pointer):
        print("cycles:", cycles)
        cycles += 1

        # Set the string 1 character
        char = string1_redux[str1_temp_pointer]
        str2_pointer = next(string2_char_positions[char])

        # chop off letters of string 2 prior to found char.
        temp_str = string2_redux[str2_pointer:]

        # Keep max len string until a longer one is found.
        temp_max_str += char
        if len(temp_max_str) > len(max_string):
            max_string = temp_max_str

        # check if string 1 is finished, continue while loop if so
        if str1_temp_pointer + 1 == len(string1_redux):
            str1_pointer += 1
            str1_temp_pointer = str1_pointer
            temp_max_str = ""
            string1_char_positions, string2_char_positions = (
                _clear_dicts(string1_char_positions, string1_redux,
                             string2_char_positions, string2_redux)
            )
            continue

        # next char to find in string1 is temp_str's next
        try:
            temp_pointer = next(string1_char_positions[temp_str[1]])
            if temp_pointer < str1_pointer:
                str1_pointer += 1
                str1_temp_pointer = str1_pointer
                temp_max_str = ""
                string1_char_positions, string2_char_positions = (
                    _clear_dicts(string1_char_positions, string1_redux,
                                 string2_char_positions, string2_redux)
                )
                continue
            elif temp_pointer < str1_temp_pointer:
                str1_pointer += 1
                continue
            else:
                str1_temp_pointer = temp_pointer
                continue
        except StopIteration:
            str1_pointer += 1
            str1_temp_pointer = str1_pointer
            temp_max_str = ""
            string1_char_positions, string2_char_positions = (
                _clear_dicts(string1_char_positions, string1_redux,
                             string2_char_positions, string2_redux)
            )

        except IndexError:
            str1_pointer += 1
            str1_temp_pointer = str1_pointer
            temp_max_str = ""
            string1_char_positions, string2_char_positions = (
                _clear_dicts(string1_char_positions, string1_redux,
                             string2_char_positions, string2_redux)
            )

    return max_string


def make_char_dict(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = (m.start() for m in re.finditer(char, string))
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
