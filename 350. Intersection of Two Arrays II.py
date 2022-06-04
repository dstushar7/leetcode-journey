# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from cmath import inf


nums1 = [1,2,2,1]
nums2 = [2]

ans = []

m = len(nums1)-1
while(m>=0):
    n = len(nums2)-1
    while (n>=0):
        if nums1[m]==nums2[n]:
            ans.append(nums1[m])
            nums1.pop(m)
            nums2.pop(n)
            break
        n-=1
    m-=1

print(ans)