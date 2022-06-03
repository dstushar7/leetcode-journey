# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# https://leetcode.com/problems/maximum-subarray/


nums = [-2,1]

# Cubic Solution : TLE Error
def cubic_subarray(nums):
    from cmath import inf

    if len(nums)==1:
        return nums[0]
    max = -inf
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum = 0
            for k in range(i,j+1):
                sum+=nums[k]
            if sum>max:
                max = sum
    return max

# Quadruple Solution : TLE Error
def quadruple_subarray(nums):
    from cmath import inf
    if len(nums)==1:
        return nums[0]
    max = -inf
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max:
                max = sum
    return max

# Linear Solution : O(n) [Kadane's Algorithm]
def linear_subarray(nums):
    sum = 0
    max = nums[0]
    for i in range(len(nums)):
        sum += nums[i]
        if sum>max:
            max = sum
        if sum<0:
            sum = 0
    return max

print(linear_subarray(nums))
