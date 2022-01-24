#!/usr/bin/env python3

"""
Python tool for encoding text to HTML entities.

Usage:
echo "your text" | python entity-everything.py
python entity-everything.py "your text"

@author: Daniel Rogowski
"""

import sys


def str_to_html_entities(str_to_convert):
    result = ""

    # Print every character's code returned by ord() function in HTML entity format
    for character in str_to_convert:
        result += f"&#{ord(character)};"

    return result


def main():
    # If no arguments passed: read text from the standard input
    # Else: take all arguments and join them to a single string
    if len(sys.argv) == 1:
        text_to_convert = sys.stdin.read()
    else:
        text_to_convert = " ".join(sys.argv[1::])

    print(str_to_html_entities(text_to_convert))


if __name__ == '__main__':
    main()
