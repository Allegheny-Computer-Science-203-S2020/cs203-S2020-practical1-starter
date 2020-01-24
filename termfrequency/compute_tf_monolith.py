"""Compute term frequencies for an input file using a monolithic style."""

import sys
import string

# the global list of [word, frequency] pairs
# pylint: disable=invalid-name
word_freqs = []
# the list of stop words
with open("stopwords/stop_words.txt") as f:
    stop_words = f.read().split(",")
# add the list of stopwords to the stop_words list
stop_words.extend(list(string.ascii_lowercase))

# iterate through the file one line at a time
for line in open(sys.argv[1]):
    start_char = None
    i = 0
    for c in line:
        if start_char is None:
            if c.isalnum():
                # We found the start of a word
                start_char = i
        else:
            if not c.isalnum():
                # We found the end of a word. Process it
                found = False
                word = line[start_char:i].lower()
                # Ignore stop words
                if word not in stop_words:
                    pair_index = 0
                    # Let's see if it already exists
                    for pair in word_freqs:
                        if word == pair[0]:
                            pair[1] += 1
                            found = True
                            break
                        pair_index += 1
                    if not found:
                        word_freqs.append([word, 1])
                    elif len(word_freqs) > 1:
                        # We may need to reorder
                        for n in reversed(range(pair_index)):
                            if word_freqs[pair_index][1] > word_freqs[n][1]:
                                # swap
                                word_freqs[n], word_freqs[pair_index] = (
                                    word_freqs[pair_index],
                                    word_freqs[n],
                                )
                                pair_index = n
                # Let's reset
                start_char = None
        i += 1

# TODO: Add the code to display the term frequencies
# NOTE: Please see the textbook for more details about this source code
