"""
String cleaning
===============

Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are
turning rabbits into zombies. He sends a text transmission to you, but it is
intercepted by a pirate, who jumbles the message by repeatedly inserting the
same word into the text some number of times.

At each step, he might have inserted the word anywhere, including at the start
or end, or even into a copy of the word he inserted in a previous step.

By offering the pirate a dubloon, you get him to tell you what that word was.

A few bottles of rum later, he also tells you that the original text was the
shortest possible string formed by repeated removals of that word,
and that the text was actually the lexicographically earliest string from all
the possible shortest candidates.

Using this information, can you work out what message your spy originally sent?

For example, if the final chunk of text was "lolol," and the inserted word was
"lol," the shortest possible strings are "ol" (remove "lol" from the beginning)
and "lo" (remove "lol" from the end). The original text therefore must have been
"lo," the lexicographically earliest string.

Write a function called answer(chunk, word) that returns the shortest,
lexicographically earliest string that can be formed by removing occurrences of
word from chunk.

Keep in mind that the occurrences may be nested, and that removing one
occurrence might result in another. For example, removing "ab" from "aabb"
results in another "ab" that was not originally present. Also keep in mind that
your spy's original message might have been an empty string.

chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.

word will have at least one character, and no more than the number of characters
in chunk.
"""

def lift(string, start, length):
    """
    Returns a string with a specified index range removed
    """
    a = start
    b = start + length
    return string[:a] + string[b:]


def rclean(subject, search, offset):
    """
    Repeatedly removes all occurrences of search starting at offset
    """

    # find the first index of the word, starting at offset
    index = subject.find(search, offset)

    length = len(search)

    # keep relacing until search can not be found in subject
    while index != -1 and offset < length:
        subject = lift(subject, index, length)
        index = subject.find(search)

    return subject


def answer(chunk, word):
    """
    Returns the shortest, lexicographically earliest string that can be formed
    by removing occurrences of word from chunk.

    This method does all replacements for each subsequent section of the string.
    """
    results = []

    for offset in range(len(chunk) - len(word)):

        # repeatedly removes all occurrences of word in chunk starting at offset
        result = rclean(chunk, word, offset)

        # check if there were any replacements
        if result != chunk:
            results.append(result)

    return sorted(results)[0]
