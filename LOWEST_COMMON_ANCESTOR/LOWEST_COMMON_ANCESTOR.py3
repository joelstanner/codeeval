# pylint: disable=R0903,C0103,R0201,W0141
"""
Write a program to determine the lowest common ancestor of two nodes in a
binary search tree. You may hardcode the following binary search tree in your
program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29

INPUT SAMPLE:

The first argument is a path to a file that contains two values.
These values represent two nodes within the tree, one per line. E.g.:

8 52
3 29

OUTPUT SAMPLE:

Print to stdout the lowest common ancestor, one per line. Lowest means the
lowest depth in the tree, not the lowest value. E.g.:

30
8
"""
from sys import argv

INPUT_FILE = argv[1]


class Tnode(object):
    """Binary Tree Node Object"""
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None


class BinaryTree(object):
    """Binary Tree implementation"""
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        """Insert the value into the tree"""
        if not self.root:
            self.root = Tnode(val)
            self.size += 1
        else:
            node = self.root
            while node:
                if val > node.val:
                    if node.right_child:
                        node = node.right_child
                    else:
                        node.right_child = Tnode(val)
                        self.size += 1
                        break
                elif val < node.val:
                    if node.left_child:
                        node = node.left_child
                    else:
                        node.left_child = Tnode(val)
                        self.size += 1
                        break
                elif node.val == val:
                    break

    def contains(self, val):
        """If node is found in tree, return list of parent nodes"""
        if not self.root:
            return []
        else:
            node = self.root
            parent_list = []
            while node:
                if val > node.val:
                    if node.right_child:
                        parent_list.append(node.val)
                        node = node.right_child
                    else:
                        return []
                elif val < node.val:
                    if node.left_child:
                        parent_list.append(node.val)
                        node = node.left_child
                    else:
                        return []
                elif node.val == val:
                    if node == self.root:
                        parent_list.append(node.val)
                    return parent_list


def parse_input(input_file):
    """Run each line through the script"""
    with open(input_file, mode="r") as file:
        for line in file:
            val1, val2 = [int(x) for x in line.rstrip().split(' ')]
            print(lowest_common_ancestor(test_tree, val1, val2))


def lowest_common_ancestor(btree, val1, val2):
    """As per challenge, find lowest common ancestor"""
    parent_list1 = btree.contains(val1)
    parent_list2 = btree.contains(val2)
    last = None
    for x, y in zip(parent_list1, parent_list2):
        if x == y:
            last = x
        else:
            break
    return last


def hardcode_tree():
    """Hard-coded tree as described in challenge description"""
    tree = BinaryTree()
    tree.insert(30)
    tree.insert(8)
    tree.insert(52)
    tree.insert(3)
    tree.insert(20)
    tree.insert(10)
    tree.insert(29)
    return tree


if __name__ == '__main__':
    test_tree = hardcode_tree()
    parse_input(INPUT_FILE)
