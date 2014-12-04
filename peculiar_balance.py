from math import log

"""
Concept:

    Complexity: O(log(n)), loops = number of steps required, calculations are O(1)

    If you break the result of a few done by hand into patterns, you will notice that for column number C,
    the pattern [R, L, -] repeats every 3 ** C times.

    We need to be able to determine which of the three steps are required.
    This is obvious and easy for the first column, because it's simply the remainder of /3.

    The same pattern can be found in the second column,
    but instead of [R, L, -] we have [R, R, R, L, L, L, -, -, -].

    The plan here is to divide that pattern into three,
    thereby giving us sections which we can now treat the same as the first column.

    The only tricky thing is that the pattern is offset by the column boundary of the previous column.
    These boundaries are at 1, 4, 13, 40 etc and can be calculated by B = 0.5 * (3 ** C - 1)
"""

# returns the number of steps required to balance the scales
def number_of_steps(starting_weight):

    # this formula was derived from B = 0.5 * (3 ** C - 1)
    return int(log(2 * starting_weight) / log(3)) + 1

def which(column, starting_weight):

    # offset correction value for column
    offset = float(3 ** column - 1) / 2

    # corrected row value to divide into sections
    corrected = (starting_weight + offset) / 3 ** column

    # section treated as first column, just need the remainder
    return int(corrected % 3)


def solve(starting_weight):

    # these will be passed to
    instructions = []

    # these are the choices corresponding to % 3
    choices = '_', 'R', 'L'

    # total number of steps required for starting weight
    steps = number_of_steps(starting_weight)

    for step in range(steps):

        # this is the choice as 0, 1 or 2
        choice = which(step, starting_weight)

        # add the corresponding choice to the instructions
        instructions.append(choices[choice])

    return instructions

def answer(x):
    return solve(x)
