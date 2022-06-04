# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# https://leetcode.com/problems/reverse-words-in-a-string-iii/


s = "Let's take LeetCode contest"

s = s.split(' ')
a = []
for i in s:
    a.append(i[::-1])
a = " ".join(a)
print(a)