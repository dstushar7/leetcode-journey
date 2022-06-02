# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# https://leetcode.com/problems/contains-duplicate/

nums = [1,2,3,1]

# Complexity O(n^2) TLE error
# for i in range(0,len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             print(True)
# print(False)


# Complexity O(nlogn)
# nums = sorted(nums)

# for i in range(0,len(nums)-1):
#     if nums[i] == nums[i+1]:
#         print(True)
# print(False)

#Complexity O(n)
if len(nums) == len(set(nums)):
    print(False)
else:
    print(True)