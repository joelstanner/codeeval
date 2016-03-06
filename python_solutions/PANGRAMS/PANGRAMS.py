"""
https://www.codeeval.com/open_challenges/37/

The sentence 'A quick brown fox jumps over the lazy dog' contains every single
letter in the alphabet. Such sentences are called pangrams. You are to write a
program, which takes a sentence, and returns all the letters it is missing
(which prevent it from being a pangram). You should ignore the case of the
letters in sentence, and your return should be all lower case letters, in
alphabetical order. You should also ignore all non US-ASCII characters.In
case the input sentence is already a pangram, print out the string NULL

INPUT SAMPLE:

    Your program should accept as its first argument a path to a filename.
This file will contain several text strings, one per line. E.g.

    A quick brown fox jumps over the lazy dog
    A slow yellow fox crawls under the proactive dog

OUTPUT SAMPLE:

    Print out all the letters each string is missing in lowercase,
alphabetical order . E.g.

    NULL
    bjkmqz
"""
from sys import argv
from string import punctuation


ALPHA = set("abcdefghijklmnopqrstuvwxyz")


def readfile(input_file):
    """Read a text file and parse it, return a list of lines."""
    lines = []
    with open(input_file, 'r') as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def missing_letters(sentence):
    """Return a sorted list of letters missing from ALPHA.

    Create a set of letters in the sentence and strip punc and whitespace.
    Return the sorted difference between this set and the letters of the
    alphabet.
    """
    set1 = set("".join(
        char for char in sentence if char not in punctuation + " ").lower()
    )
    return sorted(ALPHA - set1)


def print_output(char_list):
    """Print chars in list, NULL if empty."""
    if char_list == []:
        print("NULL")
    else:
        print(*char_list, sep="")


if __name__ == "__main__":
    lines = readfile(argv[1])
    for line in lines:
        char_list = missing_letters(line)
        print_output(char_list)
