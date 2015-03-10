"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory,
you had to develop a system to track them, since some habitually continue to
gnaw on the heads of their brethren and need extra supervision.

For obvious reasons, you based your rabbit survivor tracking system on a binary
search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages and each,
luckily enough, had a distinct age.

For a given group, the first rabbit became the root,
and then the next one (taken in order of rescue) was added,
older ages to the left and younger to the right.

The order that the rabbits returned to you determined the end pattern of
the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation,
and you need to make sure that all of the modifications or pathogens
introduced by Professor Boolean are contained properly.

Since the tree did not preserve the order of rescue, it falls to you to figure
out how many different sequences of rabbits could have produced an identical
tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1],
it would result in a binary tree identical to one created from [5, 2, 9, 1, 8].

You must write a function answer(seq) that takes an array of up to 50 integers
and returns a string representing the number (in base-10) of sequences that
would result in the same tree as the given sequence.
"""

from math import factorial

"""
Minimalistic implementation of a binary search tree.
Only supports insertion and traversal via left and right subtrees.
"""
class BST:

    def __init__(self, *values):
        """
        Creates a new binary search tree which will be empty
        unless initial values are provided, which would
        be inserted into the tree sequentially.
        """
        self.root = None
        self.left = None
        self.right = None

        # build the tree with initial values, if any.
        for value in values:
            self.insert(value)

    def insert(self, value):
        """
        Inserts a new value into the tree.
        Values are assumed to be unique.
        """
        if not self.root:
            # tree is empty, set root as value
            self.root = value

        elif value < self.root:
            # insert to the left
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)

        else:
            # insert to the right
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
Returns the number of permutations of insertion order that produces a given BST.
For example, [2, 3, 1] will create the same BST as [2, 1, 3], so there are 2.

Combine each valid permutation of a subtree with each valid permutation
of the other subtree, as a valid permutation is always the root node followed
by the combination of the valid permutations of each subtree - recursively.
"""
def input_permutations(tree):

        if not tree:
            # there is only 1 way to permute an empty tree (no input)
            return 1

        # respectively count the number of nodes in the left and right subtrees
        ls = count(tree.left)
        rs = count(tree.right)

        # recursively count the number of input permutations for each subtree
        lp = input_permutations(tree.left)
        rp = input_permutations(tree.right)

        # take the number of ways you can choose the nodes in a subtree
        # (either left or right) from all the nodes in the tree, and
        # mulitply it by the number of input permutations of each subtree.
        return choose(ls + rs, rs) * lp * rp


def answer(seq):
    return input_permutations(BST(*seq))
