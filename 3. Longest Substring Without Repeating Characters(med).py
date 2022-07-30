# Given a string s, find the length of the longest substring without repeating characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

s = "abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"

# Sliding window algorithm
unique = set()
maxlength = 0
left_pointer = 0
for r in range(len(s)):
    while s[r] in unique:
        unique.remove(s[left_pointer])
        left_pointer += 1
    unique.add(s[r])
    maxlength = max(maxlength,len(unique))
print(maxlength)