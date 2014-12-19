"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held,
but a sudden storm puts your escape plans at risk.

The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk
because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab,
you must compute how much standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top
(and allowed to run off the sides). We'll assume all the hutches are square, have side length 1,
and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

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

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list,
computes the total area of standing water accumulated as water is poured from the top and allowed to run off the sides.

The heights array will have at least 1 element and at most 9000 elements.
Each element will have a value of at least 1, and at most 100000.
"""


"""
I've tried my best to solve this problem using formulas and logic
but all my scribbles and calculations keep getting ruined in the rain.

A decision was made to employ the services of a local water rat (Pete) who
were also trapped in the lab. We made a deal that if we set him free, he will
help us determine how much standing water we're dealing with so we can all escape.

He spends a couple of minutes formulating his plan as he paces around the room:

    - He will climp to the top of the first column and find next hutch above water.
    - He will count the depths he dives to as he's swimming along to that hutch.
    - He will then sum the difference between the depths and the water's surface level.

    Eg.

       X
    X  X   X
    X XX X X
    XXXXXX X
    XXXXXXXX
    42352314

    --------------------

    Pete -->    P  X
                X  X   X
                X XX X X
                XXXXXX X
                XXXXXXXX    Total = 0

    Then dives into the water, counting how deep he goes for each column.
    He counts 2 and 1 before he comes back to the surface and climbs up at target = 3.

                   X
                XPPX   X
                XPXX X X
                XXXXXX X
                XXXXXXXX

                   P
                   X
                XOOX   X
                XOXX X X
                XXXXXX X
                XXXXXXXX    Total =  0 + 3

    He looks ahead to find either a column at his current height or higher, or simply
    the highest column he can see. In this case it's the last one at target = 7

    He dives into the water at a surface level of 4 (min(h[current], h[target])).
    He counts 2, 1 and 3 before he breaches the surface at the last column.

    He can see that there are no more hutches ahead or below him, so he's done.

                   X
                XOOXPPPX
                XOXXPXPX
                XXXXXXPX
                XXXXXXXX


                   X   P
                XOOXOOOX
                XOXXOXOX
                XXXXXXOX
                XXXXXXXX    Total = 3 + 6

    Answer = 9

"""
def answer(h):

    p = 0
    total = 0
    end = len(h)

    if end < 3:
        return 0

    # while pete has not reached the end
    while p < end - 1:

        # pete looks ahead to find either a column at his current height or higher,
        # or simply the highest column he can see.
        target = p + 1
        for index in range(p + 1, end):

            if h[index] >= h[p]:
                # he sees a hutch either on his current level
                # or higher than he is and marks his target
                target = index
                break

            if h[index] > h[target]:
                # this hutch is higher than the previous one
                # but it's possible that it's underwater, so keep looking
                target = index

        if target == p:
            # pete can't see any peak hutches ahead or below him
            # so he climbs down to report the final result
            return total

        # pete makes a note of the current surface level before he checks his scuba gear
        surface = min(h[p], h[target])

        # pete takes a dive into the murky rain water and swims one column ahead
        p += 1

        # on his way to the target...
        while p < target:

            # pete counts the difference between the surface of the water and his current depth
            total += surface - h[p]

            # as he keeps swimming across
            p += 1

    # no more hutches left
    return total
