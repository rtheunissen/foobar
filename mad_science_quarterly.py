"""
Mad science quarterly
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

class Accumulator:
    """
    Provides constant time operations for add, len and sum,
    but doesn't directly support access or removal.
    """
    def __init__(self, initial = None):
        if initial is not None:
            self._values = [initial]
            self._sum = initial
        else:
            self._values = []
            self._sum = 0

    def add(self, value):
        self._values.append(value)
        self._sum += value

    def extend(self, other):
        self._values.extend(other._values)
        self._sum += other.sum()

    def sum(self):
        return self._sum

    def __len__(self):
        return len(self._values)


class ZombitGrowthMaximizer:

    @staticmethod
    def calculate(numbers, limit):
        """
        Calculates the maximum sum of a limited-length subsequence.
        This is also known as the sliding window minimum problem.
        """

        maximum = None

        # step through each value from back to front
        for i in xrange(len(numbers) - 1, -1, -1):

            if numbers[i] < 0:
                # check max to catch the case when all numbers are negative
                maximum = max(maximum, numbers[i])
                continue

            # an accumulator to keep track of the current psotitive sum
            positives = Accumulator()

            # initialize the index for the secondary loop
            j = i

            while j >= 0 and len(positives) < limit:

                if numbers[j] >= 0:

                    # a positive value can be added to the accumulator
                    positives.add(numbers[j])

                    # update the maximum if the accumulator is greater
                    maximum = max(maximum, positives.sum())

                else:

                    # an accumulator for collecting negative values
                    negatives = Accumulator(numbers[j])

                    # accumulate any successive negative values
                    while j - 1 >= 0 and numbers[j - 1] < 0:
                        negatives.add(numbers[j - 1])
                        j -= 1

                        # break if too many negatives have been accumulated
                        if len(positives) + len(negatives) == limit:
                            break

                    if positives.sum() + negatives.sum() > 0:
                        positives.extend(negatives)
                    else:
                        # too many negatives or the negative sum was too large.
                        break

                j -= 1

        return maximum

def answer(L, k):
    return ZombitGrowthMaximizer.calculate(L, k)
