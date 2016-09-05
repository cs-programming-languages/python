#!/usr/bin/env python3
#above code is Shebang that tells which interpreter to run this module

#PEP 257 -- Docstring Conventions
# 2 black lines between functions "Sparse is better then Dense"
# Sparse means tarhasan in mongolia
# Dense means shigvv in mongolia

"""Retrieve and prints words from URL

usage:

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    :param url: The URL of a UTF-8 text document.
    :return: A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items on per line

    :param items: An iterable series of printable items
    :return: None
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    :param url: The URL of a UTF-8 text document.
    :return:
    """
    words = fetch_words(url)
    print_items(words)

# check how this module been used by checking __name__ variable if __name__ == __main__, it is used on console
if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename
