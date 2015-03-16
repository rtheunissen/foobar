"""
Undercover underground
======================

As you help the rabbits establish more and more resistance groups to fight
against Professor Boolean, you need a way to pass messages back and forth.

Luckily there are abandoned tunnels between the warrens of the rabbits,
and you need to find the best way to use them.

In some cases, Beta Rabbit wants a high level of interconnectedness,
especially when the groups show their loyalty and worthiness.

In other scenarios the groups should be less intertwined,
in case any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow,
and no two warrens should ever have more than one tunnel between them.
Your assignment: count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three
distinct ways to connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect
each warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect
N distinctly labelled warrens with exactly K tunnels, so that there is a
path between any two warrens.

The return value must be a string representation of the total number of
ways to do so, in base 10. N will be at least 2 and at most 20.
K will be at least one less than N and at most (N * (N - 1)) / 2
"""

# used for memoizing binomial coefficient calculation
mem_choose = {}

# used for memoizing total number of possible graphs for n, k
mem_graphs = {}

# used for memoizing recursive relation of counting distinct graphs
mem_counts = {}


def choose(n, k):
    """
    Calculates the binomial coefficient for n, k.
    This is equivalent to 'n choose k'.
    """
    key = (n, k)

    if key not in mem_choose:

        if k > n:
            c = 0

        elif k == 0 or n == k:
            c = 1

        elif k == 1 or k == n - 1:
            c = n

        else:
            if k > n / 2:
                k = n - k

            a = 1
            b = 1
            for t in xrange(1, k + 1):
                a *= n
                b *= t
                n -= 1

            c = a // b

        mem_choose[key] = c

    return mem_choose[key]


def possible_graphs(n, k):
    """
    Returns the total number of graphs with that can be formed using
    n nodes and k vertices. This includes graphs that are
    identical for undirected labelled graphs, as well as
    unconnected graphs.

    This function effectively returns the number of ways you can
    choose k vertices out of the 'n choose 2' possible choices.
    """
    if (n, k) not in mem_graphs:
        mem_graphs[(n, k)] = choose(n * (n - 1) >> 1, k)

    return mem_graphs[(n, k)]


def count(n, k):
    """
    Returns the number of distinct, connected, labelled, undirected
    graphs that can be formed using 'n' nodes and 'k' vertices
    """
    if (n, k) in mem_counts:
        # memoized
        return mem_counts[(n, k)]

    if k == n - 1:
        # Cayley's formula
        c = int(n ** (n - 2))

    else:

        # number of possible vertices
        p = n * (n - 1) >> 1

        if k == p:
            # only way is to connect each node to all other nodes,
            # therefore only a single distinct graph
            c = 1

        else:

            # initially all possible graphs
            c = choose(p, k)

            # there can only be duplicates or unconnected components
            # if the number of nodes is less than p - n + 2.
            # equivalent of k < (n - 1 choose 2)
            if k < p - n + 2:

                for i in range(1, n):
                    x = choose(n - 1, i - 1)

                    # minimum of possible vertices for 'i' nodes and 'k'
                    y = min(i * (i - 1) >> 1, k)

                    for j in range(i - 1, y + 1):
                        # exclude invalid graphs from the total
                        c -= x * possible_graphs(n - i, k - j) * count(i, j)

    mem_counts[(n, k)] = c
    return c


def answer(n, k):
    return count(n, k)
