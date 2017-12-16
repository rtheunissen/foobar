"""
Minglish lesson
===============

Welcome to the lab, minion. Henceforth you shall do the bidding of Professor
Boolean. Some say he's mad, trying to develop a zombie serum and all... but we
think he's brilliant!

First things first - Minions don't speak English, we speak Minglish. Use the
Minglish dictionary to learn! The first thing you'll learn is how to use the
dictionary.

Open the dictionary. Read the page numbers, figure out which pages come before
others. You recognize the same letters used in English, but the order of letters
is completely different in Minglish than English (a < b < c < ...).

Given a sorted list of dictionary words (you know they are sorted because you
can read the page numbers), can you find the alphabetical order of the Minglish
alphabet?

For example, if the words were ["z", "yx", "yz"] the alphabetical order would be
"xzy," which means x < z < y. The first two words tell you that z < y, and the
last two words tell you that x < z.

Write a function answer(words) which, given a list of words sorted
alphabetically in the Minglish alphabet, outputs a string that contains each
letter present in the list of words exactly once; the order of the letters in
the output must follow the order of letters in the Minglish alphabet.

The list will contain at least 1 and no more than 50 words, and each word will
consist of at least 1 and no more than 50 lowercase letters [a-z].

It is guaranteed that a total ordering can be developed from the input provided,
(i.e. given any two distinct letters, you can tell which is greater),
and so the answer will exist and be unique.
"""

def answer(words):

    graph = build_graph(words)
    start = start_nodes(graph)

    letters = []
    visited = []

    # Depth first graph traversal.
    def visit(node):
        if node not in visited:
            visited.append(node)

            if node in graph:
                for edge in graph[node]:
                    visit(edge)

            # Found the next letter of the alphabet
            letters.append(node)

    # Visit every starting node, depth first
    for node in start:
        visit(node)

    # Minglish complete
    return ''.join(letters[::-1])


def build_graph(words):
    """
    Start with an empty graph.
    Nodes are keys, edges are values.
    """
    graph = {}
    rows = len(words)

    # The plan here is to take pairs of words with indices
    # 0,1 -> 1,2 -> 2,3
    for row in range(rows - 1):

        # Find an edge (relationship) between two words
        edge = find_edge(words[row], words[row + 1])

        if edge is not None:
            # A valid edge could be determined,
            # so add it to the graph.

            node, direction = edge

            if node in graph:
                # The node already exists in the graph, so add the edge.
                graph[node].append(direction)
            
            else:
                # The node doesn't exist yet, so create it.
                graph[node] = [direction]

    return graph


def find_edge(a, b):

    # Minimum length of the two strings,
    length = min(len(a), len(b))

    # Keep checking across the two words until the letters are different, 
    # ie. a an edge can be created
    for c in range(length):
        if a[c] != b[c]:
            return a[c], b[c]


def start_nodes(graph):
    """
    We need to find starting nodes of the graph, which are nodes which were
    never on the right side of a relationship, ie. if we know that 'x' < 'y',
    then 'y' can not be a starting node.

    To determine this set of starting nodes we need to traverse the graph
    and only include nodes which are not present in any of the edges.
    """

    # All edges
    e = set()

    for edges in graph.values():
        for edge in edges:
            e.add(edge)

    # Starting nodes
    s = set()

    for node in graph:
        if node not in e:
            s.add(node)

    return s
