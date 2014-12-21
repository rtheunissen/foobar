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
mem = {}


"""
Helper to memoize the output of a function
"""
def memoize(key, func, *args):
    if key not in mem:
        # store the output of the function in memory
        mem[key] = func(*args)

    return mem[key]

"""
Calculates the number of arrangements of 'n' rabbits
where 'k' rabbits can be seen from the front.

n = total number of rabbits
k = number or rabbits that can be seen from the front
"""
def arrange(n, k):

    if k > n:
        # when the guard can see more rabbits than there are,
        # there are no possible valid arrangements
        return 0

    if k == n:
        # when the guard can see as many rabbits as there are,
        # there is only one arrangement (ordered)
        return 1

    if k == 1:
        # when the guard can only see one rabbit,
        # it's just the total number of permutations
        # of the rabbits behind the tallest one
        return factorial(n - 1)

    if k == n - 1:
        # when the guard can see one less than the number of rabbits,
        # the tallest has to be the second to last one, so it's just
        # the number of combinations there are of swapping the one that's
        # behind the tallest with one that's in front of the tallest.
        return combinations(n, 2)

    # memoize and return the result of the next level of recursion
    #
    # arrange(n - 1, k - 1):
    #   make one more rabbit visible by having the shortest rabbit at the front,
    #   so we're arranging (n - 1) rabbits to have (k - 1) visible from the front.
    #
    # arrange(n - 1, k) * (n - 1):
    #   have the shortest rabbit in any (n - 1) position (not at the front), so
    #   'k' does not change because there will be a taller rabbit in front of it.
    return memoize(
        (n, k),
        lambda: arrange(n - 1, k - 1) + arrange(n - 1, k) * (n - 1),
    )


"""
Returns the number of unique subsets of 'k' number of elements
that can be chosen from a set of 'n' elements.

Eg. combinations(3,2) = 3

Unique subsets of size '2' that can be made from (1,2,3):
(1,2), (1,3), (2, 3)
"""
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


"""
The concept here is to group the heights of the rabbits into subsets
consisting of one rabbit, and all succeeding rabbits before the next
visible rabbit. Excluding the tallest rabbit (n - 1), we'll have
a total number of subsets equal to 'x + y - 2'. For example,

Heights: 1,2,3,4, where x = 2 and y = 3 can be arranged as

    3,4,2,1 where the subsets are:

        --> [3],4,[2,1]
            [3,4],[2],[1] <--

    This shows that the number of subsets is equal to the number of
    rabbits that can be seen from that side.

So all we need to do is calculate how many subsets there will be,
and multiply that by the number of ways we can arrange those subsets.

x = number of rabbits that can be seen from the left
y = number of rabbits that can be seen from the right
n = total number of rabbits
"""
def answer(x, y, n):
    return arrange(n - 1, x + y - 2) * combinations(x + y - 2, x - 1)
