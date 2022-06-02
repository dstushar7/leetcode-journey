# Given an array, rotate the array to the right by k steps, where k is non-negative.

# https://leetcode.com/problems/rotate-array/

nums = [1,2,3,4,5,6,7]
k = 3

for i in range(k):
    a = nums.pop()
    nums.insert(0,a)

print(nums)
