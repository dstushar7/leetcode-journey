# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/

nums = [3,2,4]
target = 6


# Brute Force, Time consuming
def bruteforce(nums,target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j])==target:
                return [i,j]

# Hashing Technique
def hashing(nums,target):
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            return [complementMap[num],i]
        else:
            complementMap[complement] = i

print(hashing(nums,target))
