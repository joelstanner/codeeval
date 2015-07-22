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

# Most used letter is 26, 2nd most is 25, and so on.

from sys import argv

def main(input_file):
    with open(input_file, 'r') as in_file:
        for line in in_file:
            beauty = calculate_beauty(line)
            print(beauty)


def calculate_beauty(line):
    line = line.lower().rstrip()
    beauty_dict = {}
    beauty_count = 26

    for char in line:
        if char.isalpha():
            beauty_num = beauty_dict.get(char, 0)
            if beauty_num > 0:
                beauty_dict[char] = beauty_num + beauty_count
            beauty_count -= 1

    b_dict_values = beauty_dict.values()

    for val in b_dict_values:
        if val > 1:
            beauty_calc = ((val * 26) - ((val * (val + 1) // 2)) + val)
            beauty_number += beauty_calc
            print("beauty_calc:", beauty_calc, "--beauty_num:", beauty_number)
        else:
            beauty_number += 26
            print("beauty_calc:", 26, "beauty_num:", beauty_number)

    return beauty_number

if __name__ == '__main__':
    main(argv[1])
