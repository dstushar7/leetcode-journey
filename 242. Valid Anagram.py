
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_counter = Counter(s)
        second_counter = Counter(t)
        if first_counter == second_counter:
            return True
        else:
            return False