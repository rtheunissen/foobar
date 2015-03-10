"""
Zombit pandemic
===============

The nefarious Professor Boolean is up to his usual tricks.
This time he is using social engineering to achieve his
twisted goal of infecting all the rabbits and turning them
into zombits! Having studied rabbits at length, he found
that rabbits have a strange quirk: when placed in a group,
each rabbit nudges exactly one rabbit other than itself.

This other rabbit is chosen with uniform probability.
We consider two rabbits to have socialized if either or both
of them nudged the other. (Thus many rabbits could have
 nudged the same rabbit, and two rabbits may have socialized twice.)
We consider two rabbits A and B to belong to the same rabbit warren
if they have socialized, or if A has socialized with a rabbit
belonging to the same warren as B.

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

Professor Boolean realized that by infecting one rabbit,
eventually it would infect the rest of the rabbits in the same warren!
Unfortunately, due to budget constraints he can only infect one rabbit,
 thus infecting only the rabbits in one warren. He ponders,
 what is the expected maximum number of rabbits he could infect?

Write a function answer(n), which returns the expected maximum number of
rabbits Professor Boolean can infect given n, the number of rabbits.
n will be an integer between 2 and 50 inclusive.

Give the answer as a string representing a fraction in lowest terms,
in the form "numerator/denominator". Note that the numbers may be large.

For example, if there were 4 rabbits, he could infect a maximum of 2
(when they pair up) or 4 (when they're all socialized),
but the expected value is 106 / 27. Therefore the answer would be "106/27".
"""
from fractions import gcd

def expected(n):

    tp = (n - 1) ** n
    lp = (n - 1) if n % 2 == 0 else tp
    up = tp - lp if n % 2 == 0 else tp

    amin = 2
    amax = n

    num = (lp * amin) + (up * amax)
    den = tp

    g = gcd(num, den)

    return "%s/%s" % (num / g, den / g)

def answer(n):
    return expected(n)

print answer(3  )
