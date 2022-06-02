# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# https://leetcode.com/problems/contains-duplicate/

nums = [1,2,3,4]

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            print(True)
print(False)