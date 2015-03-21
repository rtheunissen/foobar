"""
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the
only known zombie cure - but there's an obstacle. The door will only open if a
challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the
left-hand side, whose mass is given in some number of units.

Predictably, the task is to  balance the two sides.
But there is a catch: You only have this peculiar weight set,
having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3.

Being a brilliant mathematician, Beta Rabbit quickly discovers that any number
of units of mass can be balanced exactly using this set. To help Beta get into
the room, write a method called answer(x), which outputs a list of strings
representing where the weights should be  placed, in order for the two sides to
be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight,
the second element to the 3-unit weight, and so on. Each string is one of:

"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight

To ensure that the output is the smallest possible, the last element of the list
must not be "-". x will always be a positive integer, no larger than 1000000000.
"""

from math import log

def number_of_steps(weight):
    """
    Returns the number of steps required to balance the scales
    """
    # this formula was derived from boundary = (3 ** n - 1) / 2
    return int(log(weight * 2, 3)) + 1


def instruction_index(n, weight):
    """
    Returns the nth instruction index for a specified starting weight
    """
    # offset correction value for n
    offset = (3 ** n - 1) / 2

    # corrected row value to divide into sections
    corrected = int((weight + offset) / 3 ** n)

    # section treated as first column, just need the remainder
    return corrected % 3


def answer(weight):
    """
    Complexity: O(log(n))

    If you break the result of a few done by hand into patterns, you will notice
    that for column number n, the pattern [R, L, -] repeats every 3 ** n times.

    We need to be able to determine which of the three steps are required.
    This is obvious and easy for the first column, because it's simply mod 3.

    The same pattern can be found in the second column,
    but instead of [R, L, -] we have [R, R, R, L, L, L, -, -, -].

    The plan here is to divide that pattern into three, thereby giving us
    sections which we can now treat the same as the first column.

    The only tricky thing is that the pattern is offset by the column boundary
    of the previous column. These boundaries are at 1, 4, 13, 40 etc and can
    be calculated by using (3 ** n - 1) / 2.
    """

    instructions = []

    # total number of steps required for starting weight
    steps = number_of_steps(weight)

    for n in xrange(steps):

        # the index of the instruction, corresponding to the choices
        i = instruction_index(n, weight)

        # add the corresponding choice to the list of instructions
        instructions.append(['-', 'R', 'L'][i])

    return instructions
