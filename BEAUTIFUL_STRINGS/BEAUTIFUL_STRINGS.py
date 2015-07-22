"""
BEAUTIFUL STRINGS
CHALLENGE DESCRIPTION:


Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.

When John was a little kid he didn't have much to do. There was no internet,
no Facebook, and no programs to hack on. So he did the only thing he could...
he evaluated the beauty of strings in a quest to discover the most beautiful
string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of
the beauty of the letters in it. The beauty of each letter is an integer between
1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't
care about whether letters are uppercase or lowercase, so that doesn't affect
the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f',
for example.)

You're a student writing a report on the youth of this famous hacker. You found
the string that Johnny considered most beautiful. What is the maximum possible
beauty of this string?

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each
line in this file has a sentence. E.g.

ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

OUTPUT SAMPLE:

Print out the maximum beauty for the string. E.g.

152
754
491
729
646
"""

# Every time a letter is used, it is 26 beauty. Each subsequent use of a
# letter is 26 minus 1 for how many times it has already been used

from sys import argv


def main(input_file):
    with open(input_file, 'r') as in_file:
        for line in in_file:
            beauty = calculate_beauty(line)
            print(beauty)


def calculate_beauty(line):
    line = line.lower().rstrip()
    beauty_dict = {}

    for char in line:
        if char.isalpha():
            char_count = beauty_dict.get(char, 0)
            beauty_dict[char] = char_count + 1

    b_dict_sort = sorted(beauty_dict.values(), reverse=True)

    beauty_num = 26
    beauty_total = 0

    for val in b_dict_sort:
        beauty_total += val * beauty_num
        beauty_num -= 1

    return beauty_total

if __name__ == '__main__':
    main(argv[1])
