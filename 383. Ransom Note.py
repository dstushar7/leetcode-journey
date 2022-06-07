# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# https://leetcode.com/problems/ransom-note/



from collections import Counter

ransomNote = "a"
magazine = "b"
magazineCounter = Counter(magazine)
for i in ransomNote:
    if i in magazineCounter:
        magazineCounter[i] -= 1
        if magazineCounter[i] == 0:
            del magazineCounter[i]
    else:
        print(False)
print(True)