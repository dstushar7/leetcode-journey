# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

# https://leetcode.com/problems/first-bad-version/


# It works with an API, so I'll just copy paste my code from Leetcode



# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        ans = -1 
        while(start<=end):
            mid = (start+end)//2
            if (isBadVersion(mid)==True):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans