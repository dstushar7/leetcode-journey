# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1

# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


def firstUnique(s):
    unique_items = Counter(s)
    for i in range(len(s)):
        if unique_items[s[i]] == 1:
            return i
    return -1

print(firstUnique("leetcode"))