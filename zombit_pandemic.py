"""
Zombit pandemic
===============

The nefarious Professor Boolean is up to his usual tricks. This time he is
using social engineering to achieve his twisted goal of infecting all the
rabbits and turning them into zombits! Having studied rabbits at length,
he found that rabbits have a strange quirk: when placed in a group,
each rabbit nudges exactly one rabbit other than itself.
This other rabbit is chosen with uniform probability. We consider two
rabbits to have socialized if either or both of them nudged the other.
(Thus many rabbits could have nudged the same rabbit, and two rabbits
    may have socialized twice.) We consider two rabbits A and B to belong
to the same rabbit warren if they have socialized, or if A has socialized
with a rabbit belonging to the same warren as B.

For example, suppose there were 7 rabbits in Professor Boolean's nefarious lab.
We denote each rabbit using a number. The nudges may be as follows:

1 nudges 2
2 nudges 1
3 nudges 7
4 nudges 5
5 nudges 1
6 nudges 5
7 nudges 3

This results in the rabbit warrens {1, 2, 4, 5, 6} and {3, 7}.

Professor Boolean realized that by infecting one rabbit, eventually it would
infect the rest of the rabbits in the same warren! Unfortunately, due to
budget constraints he can only infect one rabbit, thus infecting only the
rabbits in one warren. He ponders, what is the expected maximum number of
rabbits he could infect?

Write a function answer(n), which returns the expected maximum number of
rabbits Professor Boolean can infect given n, the number of rabbits.

n will be an integer between 2 and 50 inclusive. Give the answer as a string
representing a fraction in lowest terms, in the form "numerator/denominator".
Note that the numbers may be large.

For example, if there were 4 rabbits, he could infect
a maximum of 2 (when they pair up) or 4 (when they're all socialized),
but the expected value is 106 / 27. Therefore the answer would be "106/27".
"""

from math import factorial
from operator import mul
from fractions import gcd

# used for memoizing the total number of single-tree connected forests
mem_single = {}

# used for memoizing binomial coefficient calculations
mem_choose = {}

"""
Returns the number of pseudoforests with exactly one connected component
involving all the nodes, ie. all nodes connected by a single tree.
'A000435' requires float division, so I'm using 'A001864 / n' instead.
"""
def S(n):
    if n not in mem_single:
        mem_single[n] = \
            sum(choose(n, k) * (n - k) ** (n - k)* k ** k for k in range(1, n)) / n

    return mem_single[n]

"""
Calculates the binomial coefficient for n, k.
This is equivalent to 'n choose k'.

http://stackoverflow.com/a/3025547/374865
"""
def binomial(n, k):
    if k > n:
        return 0

    elif k == 0 or n == k:
        return 1

    elif k == 1 or k == n - 1:
        return n

    else:
        if k > n >> 1:
            k = n - k

        a = 1
        b = 1
        for t in range(1, k + 1):
            a *= n
            b *= t
            n -= 1

        return a // b


"""
Memoized binomial coefficient to count combinations
"""
def choose(n, k):
    if (n, k) not in mem_choose:
        mem_choose[(n, k)] = binomial(n, k)

    return mem_choose[(n, k)]


# Returns the number of ways n labelled items can be split according to a given partition
def C(n, partition):

    num = 1
    s = 0

    # counts the number of ways of splitting n labelled nodes into connected components
    # of the sizes given by the partition
    for i in range(len(partition)):
        num *= choose(n - s, partition[i])
        s += partition[i]

    # multiplicities of each member of the partition
    m = [partition.count(p) for p in set(partition)]

    # multiplication reduction of the factorial of each multiplicity
    den = reduce(mul, map(factorial, m))

    return num / den


# Generates all integer partitions of n
def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while x << 1 <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            p = a[:k + 2]

            # ignore all trees of one node
            if 1 not in p:
                yield p

            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        p = a[:k + 1]

        # ignore all trees of one node
        if 1 not in p:
            yield p


"""
Calculates the numerator of the answer
"""
def numerator(n):
    return sum(max(p) * C(n, p) * reduce(mul, map(S, p)) for p in partitions(n))


def answer(n):

    num = numerator(n)

    # denominator is the total number of forests for N
    den = (n - 1) ** n

    # reduce the fraction using the greatest common divisor
    div = gcd(num, den)

    return "%d/%d" % (num / div, den / div)
