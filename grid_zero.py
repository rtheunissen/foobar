"""
Grid Zero
=========

You are almost there. The only thing between you and foiling Professor Boolean's
plans for good is a square grid of lights, only some of which seem to be lit up.

The grid seems to be a lock of some kind. That's interesting. Touching a light
toggles the light, as well as all of the other lights in the same row and column
as that light.

Wait! The minions are coming - better hide.

Yes! By observing the minions, you see that the light grid is, indeed, a lock.
The key is to turn off all the lights by touching some of them. The minions are
gone now, but the grid of lights is now lit up differently. Better unlock it
fast, before you get caught.

The grid is always a square. You can think of the grid as an NxN matrix of
zeroes and ones, where one denotes that the light is on, and zero means that the
light is off.

For example, if the matrix was

1 1
0 0

Touching the bottom left light results in

0 1
1 1

Now touching the bottom right light results in

0 0
0 0

...which unlocks the door.

Write a function answer(matrix) which returns the minimum number of lights that
need to be touched to unlock the lock, by turning off all the lights. If it is
not possible to do so, return -1.

The given matrix will be a list of N lists, each with N elements.
Element matrix[i][j] represents the element in row i, column j of the matrix.

Each element will be either 0 or 1, 0 representing a light that is off, and 1
representing a light that is on.

N will be a positive integer, at least 2 and no more than 15.
"""

import itertools

def answer(matrix):
    """
    Determines the minimum number of switches required to turn off all the
    lights in a given matrix configuration.
    """
    N = len(matrix)  # Size of the matrix
    R = range(N)     # Iteration range across the matrix


    # Calculate the sum of each row and column.
    row_sums = []
    col_sums = []
    for i in R:
        row_sums.append(sum(matrix[i]))
        col_sums.append(sum(matrix[j][i] for j in R))


    def point_parity_sum(matrix):
        """
        Calculates the sum of the parities of each point's row and column sum.

        Eg. if a point at x,y has a bit sum of 6 (col + row - point), that point
            has a parity of 0, and doesn't contribute to the parity sum.
        """
        S = 0
        P = range(len(matrix))  # Can't use R because it was calculated before
                                # a potential padding in the odd size case.

        # For each point in the matrix, combine the sums of its row and column,
        # but subtract the point itself to negate counting the point twice.
        for row in P:
            for col in P:
                S += (row_sums[row] + col_sums[col] - matrix[row][col]) & 1

        return S


    # If the grid size is even, the smallest number of switches will be the sum
    # of the parities of each point's row and column sum.
    #
    # All configurations where the size is even can be solved, because you can
    # switch any light by switching all the lights in its row and column.
    if not N & 1:
        return point_parity_sum(matrix)

    # When the size of the grid is odd, the sum of all rows and columns must
    # have the same parity for a solution to exist.
    if len(set(x & 1 for x in row_sums + col_sums)) != 1:
        return -1

    result = None

    # Pad each row with a 0, creating an empty column.
    for row in matrix:
        row.append(0)

    # We have to brute force the padded row, adjust the padded column, and find
    # the solution with the fewest required switches that doesn't involve any
    # switches in the padded row or column.
    for permutation in itertools.product([0, 1], repeat=N):

        # Only use permutations where the row parity matches the other rows.
        if sum(permutation) & 1 != row_sums[0] & 1:
            continue

        # Padding the odd matrix to N+1 will require an extra slot for each sum.
        col_sums.append(0)
        row_sums.append(0)

        # Bottom right corner must be 0, otherwise it guarantees that a switch
        # is required in either the bottom row or the last column.
        permutation += (0,)

        # The candidate row contributes to the column sums.
        for i in R:
            col_sums[i] += permutation[i]

        # We have to calculate what the values of the column padding will be,
        # such that we won't need to switch any lights in that column.
        #
        # Every row parity has to be even where the padding column has a 1.
        for i in R:

            # We have to determine the parities of each point in the row to
            # determine whether we need to switch the column light or not.
            F = 0
            for j in R:
                F += (row_sums[i] + col_sums[j] - matrix[i][j]) & 1

            # If there are more 1's than 0's in the row point parity sum, we
            # know that the row will be flipped in the solution, so we can use
            # a one and know that it'll be flipped to a zero, therefore we know
            # that we wouldn't need to switch the padded point.
            flip = 1 if F > N >> 1 else 0

            matrix[i][N] = flip

            if flip:
                row_sums[i] += 1
                col_sums[N] += 1


        # Add the row candidate to the matrix.
        matrix.append(permutation)

        # Set the row sum for the bottom row (the solution candidate row).
        row_sums[N] = sum(permutation)

        # Solution candidate.
        candidate = point_parity_sum(matrix)

        # We're looking for the best candidate, so keep track of the smallest.
        if candidate < result or result is None:
            result = candidate

        # We have to reset the row and column sums for the next permutation.
        for i in R:
            row_sums[i] -= matrix[i][N]
            col_sums[i] -= matrix[N][i]

        matrix.pop()
        col_sums.pop()
        row_sums.pop()

    # Remove the padded column values from each row, so that we don't leave the
    # provided matrix in a different state than we received it.
    for row in matrix:
        row.pop()

    return result
