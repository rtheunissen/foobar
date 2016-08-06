"""
Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored
minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a
horizontal row. The minion places a token on the left-most square and rolls a
special three-sided die.

If the die rolls a "Left", the minion moves the token to a square one space
to the left of where it is currently. If there is no square to the left,
the game is invalid, and you start again.

If the die rolls a "Stay", the token stays where it is.

If the die rolls a "Right", the minion moves the token to a square, one space
to the right of where it is currently. If there is no square to the right,
the game is invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on
the last roll. If you land on the rightmost square before t rolls are done then
the only valid dice roll is to roll a "Stay". If you roll anything else, the
game is invalid (i.e., you cannot move left or right from the rightmost square).

To make it more interesting, the minions have leaderboards
(one for each n,t pair) where each minion submits the game he just played:
the sequence of dice rolls. If some minion has already submitted the exact
same sequence, they cannot submit a new entry, so the entries in the
leader-board correspond to unique games playable.

Since the minions refresh the leaderboards frequently on their mobile
devices, as an infiltrating hacker, you are interested in knowing the
maximum possible size a leaderboard can have.

Write a function answer(t, n), which given the number of dice rolls t, and the
number of squares in the board n, returns the possible number of unique games
modulo 123454321. i.e. if the total number is S, then return the remainder upon
dividing S by 123454321, the remainder should be an integer between 0 and
123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.
"""

def answer(t, n):

    # Create an empty state accumulator, with an extra space on the left avoid
    # the need to check for bounds on the left. We can just ignore it.
    acc = [0] * (n + 1)

    # The initial state is where the token is on square one.
    acc[1] = 1

    # Update the state for every roll, keeping track of the number of ways we
    # can get to each square up to that stage.
    for k in xrange(t):

        # Create an empty state to keep track of this roll's contribution
        # to the accumulated state.
        tmp = [0] * (n + 1)

        # The total number of possiblities carries over into the last square.
        tmp[n] = acc[n]

        # We want to update the number of possible sequences to get to k,
        # while also taking backtracking into account.
        for pos in xrange(max(1, n - t + k), n):

            # Update each square's possible movements.
            for move in (-1, 0, 1):
                tmp[pos + move] += acc[pos]

        # The temporary state becomes the new accumulated state.
        acc = tmp

    # The total number of possible sequences will be in the last square of the
    # accumulated state (to get to that square), so return the requested mod.
    return acc[n] % 123454321


"""
Recursive solution - far too slow.
"""
# LEFT  = -1
# STAY  =  0
# RIGHT =  1

# def play(move, distance, distance_to_go, moves_remaining):
#
#     moves_remaining -= 1      # Decrease the number of moves to go
#     distance_to_go  -= move   # Update how far from the target we are
#     distance        += move   # Update how far we have moved from zero

#     # Can't complete the game or moving off the edge
#     if (moves_remaining < distance_to_go) or (distance < 0):
#         return 0

#     # No moves left or have to stay
#     if (moves_remaining == 0) or (distance_to_go == 0):
#         return 1

#     return play(RIGHT, distance, distance_to_go , moves_remaining) \
#          + play(STAY,  distance, distance_to_go , moves_remaining) \
#          + play(LEFT,  distance, distance_to_go , moves_remaining)

# def answer(moves_remaining, size):
#     return play(RIGHT, 0, size - 1, moves_remaining) \
#          + play(STAY,  0, size - 1, moves_remaining)
