"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory,
you had to develop a system to track them, since some habitually continue to gnaw on the heads of
their brethren and need extra supervision.

For obvious reasons, you based your rabbit survivor tracking system on a binary search tree,
but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age.
For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added,
older ages to the left and younger to the right.

The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation,
and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean
are contained properly. Since the tree did not preserve the order of rescue,
it falls to you to figure out how many different sequences of rabbits could have produced
an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1],
it would result in a binary tree identical to one created from [5, 2, 9, 1, 8].

You must write a function answer(seq) that takes an array of up to 50 integers and returns a
string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.
"""

from math import factorial


"""
Minimal implementation of a binary search tree.
"""
class BST:

    def __init__(self, *values):
        self.root = None
        self.left = None
        self.right = None

        for value in values:
            self.insert(value)

    def insert(self, value):

        if not self.root:
            self.root = value
        else:
            if value < self.root:
                # left
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BST(value)
            else:
                # right
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BST(value)



"""
Calculates the binomial coefficient for n, k.
This is equivalent to 'n choose k'.
"""
def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


"""
Returns the total number of nodes in a tree, including the root.
"""
def count(tree):
    return 1 + count(tree.left) + count(tree.right) if tree else 0


"""
Returns the number of distinct import orders that produce the given binary tree.






"""
def input_permutations(tree):

        if not tree:
            #
            return 1

        #
        ls = count(tree.left)
        rs = count(tree.right)

        #
        lp = input_permutations(tree.left)
        rp = input_permutations(tree.right)

        #
        #
        return choose(ls + rs, ls) * lp * rp


def answer(seq):
    return input_permutations(BST(*seq))


print answer([6,2,3,1,5,4,8,9,7,13,11,20,15,16,17,14,12,19,18,25,24,23,22,21])
