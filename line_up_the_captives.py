"""
Line up the captives
====================

As you ponder sneaky strategies for assisting with the great rabbit escape, you realize that you have an opportunity
to fool Professor Booleans guards into thinking there are fewer rabbits total than there actually are.

By cleverly lining up the rabbits of different heights, you can obscure the sudden departure of some of the captives.

Beta Rabbits statisticians have asked you for some numerical analysis of how this could be done
so that they can explore the best options.

Luckily, every rabbit has a slightly different height, and the guards are lazy and few in number.
Only one guard is stationed at each end of the rabbit line-up as they survey their captive population.

With a bit of misinformation added to the facility roster,
you can make the guards think there are different numbers of rabbits in holding.

To help plan this caper you need to calculate how many ways the rabbits can be lined up
such that a viewer on one end sees x rabbits, and a viewer on the other end sees y rabbits,
because some taller rabbits block the view of the shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm, 50 cm, 40 cm, and then 20 cm,
a guard looking from the left would see 2 rabbits while a guard looking from the right side would see 3 rabbits.

Write a method answer(x,y,n) which returns the number of possible ways to arrange n rabbits of unique heights
along an east to west line, so that only x are visible from the west, and only y are visible from the east.
The return value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1 and as large as the total number of rabbits (n).
"""

from math import factorial

# used for memoization of recursively calculating sterling numbers
cache = {}


# unsigned stirling numbers of the first kind
def s1(n, m):

    # base cases for the recursion are:
    # 1 when n && m are 0
    # 0 when n || m are 0
    if n == 0 or m == 0:
        return n == m

    # check if we have already calculated the current level of recursion
    if (n, m) not in cache:

        # recursively calculate to cache
        cache[n, m] = (n - 1) * s1(n - 1, m) + s1(n - 1, m - 1)

    return cache[n, m]


# binomial coefficients, ie n choose k
def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def answer(x, y, n):
    #
    #
    return s1(n - 1, x + y - 2) * binomial(x + y - 2, x - 1)
