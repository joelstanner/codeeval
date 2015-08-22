"""Write a program which reads a file and prints to stdout the specified
number of the longest lines that are sorted based on their length in
descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file
contains multiple lines. The first line indicates the number of lines you
should output, the other lines are of different length and are presented
randomly. You may assume that the input file is formatted correctly and the
number in the first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their
length in descending order.

For example:

San Francisco
Hello World
"""

from sys import argv


INPUT_FILE = argv[1]


def longest_lines(input_file):
    with open(input_file, "r") as f:
        final_list = []
        min_len = 0  # mimumum len to be considered
        output_lines_num = int(f.readline())

        for line in f:
            line = line.rstrip()
            if len(line) > min_len:
                # Keep adding if list is not full
                if len(final_list) < output_lines_num:
                    final_list.append(line)
                else:
                    final_list[-1] = line
                    final_list.sort(key=lambda x: len(x), reverse=True)
                    min_len = len(final_list[-1])

        for item in final_list:
            print(item)


if __name__ == '__main__':
    longest_lines(INPUT_FILE)
