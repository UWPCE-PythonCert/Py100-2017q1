#!/usr/bin/python

# Trigram analysis is very simple. Look at each set
# of three adjacent words in a document. Use the
# first two words of the set as a key, and remember
# the fact that the third word followed that key.
# Once you’ve finished, you know the list of individual
# words that can follow each two word sequence in the document.

# Kata’s are about trying something many times.
# In this one, what we’re experimenting with is not just the code,
# but the heuristics of processing the text. What do we do with punctuation?
# Paragraphs? Do we have to implement backtracking if we
# chose a next word that turns out to be a dead end?

trigrams = []

count = 2

def kata():
    """Compose a kata from text document."""

    with open('sherlock_small.txt') as text_file:
        for line in text_file:
            print(line)

        while count < 2:
            pass


if __name__ == '__main__':
    kata()