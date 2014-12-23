"""
Undercover underground
======================

As you help the rabbits establish more and more resistance groups to fight against Professor Boolean, you need a way to pass messages back and forth.


Luckily there are abandoned tunnels between the warrens of the rabbits, and you need to find the best way to use them. In some cases, Beta Rabbit wants a high level of interconnectedness, especially when the groups show their loyalty and worthiness. In other scenarios the groups should be less intertwined, in case any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow, and no two warrens should ever have more than one tunnel between them. Your assignment: count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three distinct ways to connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect each warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect N distinctly labelled warrens with exactly K tunnels, so that there is a path between any two warrens.

The return value must be a string representation of the total number of ways to do so, in base 10.
N will be at least 2 and at most 20.
K will be at least one less than N and at most (N * (N - 1)) / 2

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) N = 2
    (int) K = 1
Output:
    (string) "1"

Inputs:
    (int) N = 4
    (int) K = 3
Output:
    (string) "16"
"""

from math import factorial
from string import ascii_uppercase
from itertools import combinations, permutations


def number_of_combinations_that_are_not_valid(N, K):

    nodes = [ascii_uppercase[x] for x in range(N)]

    edges = [x for x in combinations(nodes, 2)]

    combs = combinations(edges, K)

    invalid_count = 0

    for c in combs:
        reach = set([node for edges in c for node in edges])
        for node in nodes:
            if node not in reach:
                invalid_count += 1

    return invalid_count

def links_all_nodes(permutation, nodes):

    required = set([node for edges in permutation for node in edges])

    # we want to count the number of combinations that do not
    # link to all nodes

    for node in nodes:
        if node not in required:
            return False
    return True

def force(N, K):

    nodes = [ascii_uppercase[x] for x in range(N)]

    edges = [x for x in combinations(nodes, 2)]

    valid = set()

    for p in combinations(edges, K):

        if links_all_nodes(p, nodes):
            p = tuple(sorted(p))
            if p[::-1] not in valid:
                valid.add(p)

    return len(valid)



    # graph = []

    # for j in range(N):

    #     letters = [alpha[x] for x in range(0, N)] + [alpha[j]]
    #     permutations = itertools.permutations(letters)

    #     for p in permutations:

    #         edges = []

    #         for i in range(N):
    #             a = p[i]
    #             b = p[i + 1]
    #             edge = sorted([a, b])
    #             if edge not in edges and a != b:
    #                 edges.append(edge)

    #         a = p[i]
    #         b = p[-1]
    #         edge = sorted([a, b])
    #         if edge not in edges and a != b:
    #             edges.append(edge)

    #         edges = sorted(edges)
    #         if edges not in graph and len(edges) == K:
    #             print edges
    #             graph.append(edges)

    # return len(graph)

def p(N, K):
    return factorial(N) / factorial(N - K)

def c(N, K):
    return factorial(N) / (factorial(K) * factorial(N - K))

def answer(N, K):

    U = N * (N - 1) / 2

    if K == U:
        return 1

    if N > 3:

        a = U - K - 1

        F = factorial(a) / factorial(K - 1)

        d = N * (F / (N - 1))


        return c(U, K) - d

    # if K == N:
    #     # same number of tunnels are there are nodes
    #     # this

    #     return p(U, K) / (factorial(K))

print number_of_combinations_that_are_not_valid(6,11)


# for i in range(4, 8):
#     ex =  force(5, i)
#     ac = answer(5, i)
#     print "%s,%s:" % (5, i)
#     print "%s, %s, %s" % (ex, ac, ex - ac)
#     print "----"

# for i in range(5, 8):
#     ex =  force(6, i)
#     ac = answer(6, i)
#     print "%s,%s:" % (6, i)
#     print "%s, %s, %s" % (ex, ac, ex - ac)
#     print "----"

# print force(5, 5)
# print answer(5, 5)
