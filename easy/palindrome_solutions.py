#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Original solution - clear and readable
    code = code.lower()
    filteredcode = [c for c in code if c.isalpha()]
    return filteredcode == filteredcode[::-1]


def isAlphabeticPalindrome_oneliner(code):
    # One-line solution using list comprehension
    return (filtered := [c.lower() for c in code if c.isalpha()]) == filtered[::-1]


def isAlphabeticPalindrome_string(code):
    # String-based approach (join filtered chars into a string)
    filtered = ''.join(c.lower() for c in code if c.isalpha())
    return filtered == filtered[::-1]


def isAlphabeticPalindrome_filter(code):
    # Using filter() function instead of list comprehension
    filtered = list(filter(str.isalpha, code.lower()))
    return filtered == filtered[::-1]


def isAlphabeticPalindrome_regex(code):
    # Using regex to extract only alphabetic characters
    filtered = re.findall(r'[a-zA-Z]', code.lower())
    return filtered == filtered[::-1]


def isAlphabeticPalindrome_twopointer(code):
    # Two-pointer approach (no extra space for reversed list)
    # More memory efficient for very long strings
    filtered = [c.lower() for c in code if c.isalpha()]
    left, right = 0, len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
    return True


def isAlphabeticPalindrome_twopointer_nofilter(code):
    # Two-pointer approach without creating filtered list
    # Skips non-alphabetic characters on the fly - O(1) space!
    code = code.lower()
    left, right = 0, len(code) - 1

    while left < right:
        # Skip non-alphabetic characters from left
        while left < right and not code[left].isalpha():
            left += 1

        # Skip non-alphabetic characters from right
        while left < right and not code[right].isalpha():
            right -= 1

        # Compare alphabetic characters
        if code[left] != code[right]:
            return False

        left += 1
        right -= 1

    return True


def isAlphabeticPalindrome_ascii(code):
    # Using ASCII values for case-insensitive comparison
    # A-Z: 65-90, a-z: 97-122 (difference of 32)
    # Uppercase letters can be converted by OR-ing with 32 (sets bit 5)
    left, right = 0, len(code) - 1

    while left < right:
        # Skip non-alphabetic characters from left
        while left < right and not code[left].isalpha():
            left += 1

        # Skip non-alphabetic characters from right
        while left < right and not code[right].isalpha():
            right -= 1

        # Convert both to lowercase using ASCII bit manipulation
        # ord(c) | 32 converts uppercase to lowercase (sets bit 5)
        # For lowercase letters, bit 5 is already set, so no change
        left_char = ord(code[left]) | 32
        right_char = ord(code[right]) | 32

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
