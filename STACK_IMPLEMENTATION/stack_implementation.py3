# pylint: disable=R0903
"""
Write a program which implements a stack interface for integers. The interface
should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a series of
integers and then ‘pop’ and print every alternate integer.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains a
series of space delimited integers, one per line.

For example:
1 2 3 4
10 -2 3 4

OUTPUT SAMPLE:

Print to stdout every alternate space delimited integer, one per line.

For example:
4 2
4 -2
"""

from sys import argv

INPUT_FILE = argv[1]


def parse_input(input_file):
    """Read each line of a file and do stuff with it"""
    with open(input_file, mode="r") as file:
        for line in file:
            ints = [int(x) for x in line.split()]
            working_stack = Stack()
            # Push the numbers, pop off and print the alternates
            pointer = 1  # used to determine "every other" status

            for number in ints:
                working_stack.push(number)

            while True:
                try:
                    if pointer % 2:  # print only odd number pointer items
                        print(working_stack.pop(), end=" ")
                    else:
                        working_stack.pop()
                    pointer += 1
                except ValueError:
                    break
            print()


class Stack:
    """Implements a stack data structure"""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Take a data element and put it on the top of the stack"""
        self.top = Item(data, self.top)

    def pop(self):
        """Remove the top item from the stack, and return the value of it"""
        prev_top = self.top
        try:
            self.top = self.top.next_item
        except AttributeError:
            raise ValueError("The stack is empty")

        return prev_top.data


class Item:
    """Wrapper for a data item that get pushed on the stack"""

    def __init__(self, data, next_item=None):
        self.data = data
        self.next_item = next_item


if __name__ == '__main__':
    parse_input(INPUT_FILE)
