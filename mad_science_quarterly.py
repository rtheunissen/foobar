"""
Mad Science Quarterly
=====================

The deadline for submitting papers to the Mad Science Quarterly is approaching.
Professor Boolean's topic: On the Rate of Growth of Zombie Rabbits.

In the lab, Boolean's minions recorded the net growth of the number of zombits
for each day, which is the number of births minus the number of deaths (yes,
zombits do die). He realized that if these figures were to be added up over
time, it would seem like the zombits multiplied very quickly.

Then everyone shall be convinced of his mad genius! He would proudly display
these figures in his paper. Since some of the figures may be negative,
and larger numbers are more convincing, Professor Boolean will choose which
figures to show so that the sum is maximized. However, he must show a sequence
of consecutive figures without omitting the unfavorable ones - Professor Boolean
also needs to be scientific, you see.

Unfortunately, the Mad Science Quarterly limits how much data can be
shown - it is, after all, Mad. This means the mad doctor can display no more
than a certain number of figures.

Write a function answer(L, k) which returns the maximum sum Professor Boolean
can obtain by choosing some consecutive figures from his data. L will be a list
of integers representing his data, the daily net growth of the number of zombits
over a period of time. k will be the maximum number of figures he can display.

Each element of L will have absolute value no greater than 100. L will contain
at least 2 and no more than 7000 elements, and at least one element will be
positive. k will be an integer, at least 3 and no greater than the length of L.
"""

class ZombitGrowthMaximizer:

    def calculate(numbers, limit):
        """
        Calculates the maximum growth metric that can be obtained from
        a given set of values, given a limit on how many consecutive
        numbers are allowed to be used.
        """

        # used to store the maximum sum during the iteration
        maximum = None

        # step through each value from back to front
        for i in xrange(len(values) - 1, -1, -1):

            if values[i] < 0:
                # check max to catch the case when all numbers are negative
                maximum = max(maximum, values[i])
                continue

            # initialize the index for the secondary loop
            j = i

            # an accumulator to keep track of the current sum
            acc = 0

            # the number of values that have been added to the accumulator
            count = 0

            # keep looping as long as there are numbers ahead,
            # and if we haven't reached the limit yet
            while j >= 0 and count < limit:

                if values[j] >= 0:

                    # a positive value can be added to the accumulator
                    acc += values[j]
                    count += 1

                    # update the maximum if the accumulator is greater
                    maximum = max(maximum, acc)

                else:
                    # a negative value

                    # an accumulator for collecting negative values
                    nacc = values[j]
                    ncount = 1

                    # accumulate any successive negative values
                    while j - 1 >= 0 and values[j - 1] < 0:
                        nacc += values[j - 1]
                        ncount += 1
                        j -= 1

                    # if the sum of the negative accumulator doesn't
                    # negate the positive accumulator and the number
                    # of values that contributed to the negative sum
                    # doesn't break the limit, update the positive
                    # accumulator with the negative sum
                    if acc + nacc > 0 and count + ncount < limit:
                        count += ncount
                        acc += nacc
                    else:
                        # either a run of negatives broke past the limit,
                        # or the negative sum was too large.
                        break

                # continue on to the next index
                j -= 1

        return maximum

def answer(L, k):
    return ZombitGrowthMaximizer.calculate(L, k)
