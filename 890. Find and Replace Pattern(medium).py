# Given a list of strings words and a string pattern, 
# return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x),
# we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, 
# and no two letters map to the same letter.

# https://leetcode.com/problems/find-and-replace-pattern/



words = ["a","b","c"]
pattern = "a"

unique = len(set(pattern))
result = []
for word in words:
    i = -1
    check_dict = dict() # To map strings to pattern
    if len(set(word))==unique:
        for letter in word:
            i += 1
            if check_dict.get(pattern[i])==None:
                check_dict[pattern[i]]=letter
            else:
                if check_dict[pattern[i]]!=letter:
                    break
            if i==(len(pattern)-1):
                result.append(word)
print(result)