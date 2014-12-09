"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list, computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides.

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
"""
def answer(heights):
    return two_rats_go_for_a_swim(heights)

"""
I've tried my best to solve this problem using formulas and logic
but all my scribbles and calculations keep getting ruined in the rain.

A decision was made to employ the services of a couple of keen water rats (Fats and Slim) who
were also trapped in the lab. We made a deal that if we set them free, they will
help us determine how much standing water we're dealing with so we can all escape.

They spend a couple of minutes whispering to each other before they let us in on their plan:

    - They will climp to the top of the first column, and swim across to the last one.
    - Fats is the better swimmer so he will dive into the water and keep track of the depths.
    - When he returns to the surface, Slim will paddle across to him and add up his numbers.

"""
def two_rats_go_for_a_swim(h):

    slim = 0
    fats = 0
    total = 0
    end = len(h)

    if end < 3:
        return 0

    # while fats has not reached the end of the stack
    while fats < end - 1:

        # fats tries to look ahead to see where he should be swimming to
        target = fats + 1
        for index in range(fats + 1, end):

            # fats and slim can see the top of a hutch above them
            if h[index] >= h[fats]:
                target = index
                break

            # fats and slim can see the top of a hutch below them
            # but are still looking ahead for a better target
            if h[index] > h[target]:
                target = index

        if target == fats:
            # fats can see that the rest of the water spills down to the floor
            # so what they've counted so far has to be the final amount
            return total

        # slim makes a note of the current surface level while fats checks his scuba gear
        surface = min(h[slim], h[target])

        # fats takes a dive into the murky rain water and swims one box ahead
        fats += 1

        # while has not yet reached his target
        while fats < target:

            # fats counts the difference between the surface of the water his current depth
            total += surface - h[fats]

            # fats swims ahead
            fats += 1

        # slim paddles across the water to catch up to fats
        slim = fats

    return total
