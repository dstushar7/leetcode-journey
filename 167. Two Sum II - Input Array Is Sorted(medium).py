# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

numbers = [2,7,11,15]
target = 9

def bruteforce(nums,target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j])==target:
                return [i,j]

def pointer_approach(numbers,target):
    i = 0
    j = len(numbers)-1
    while i<j:
        if target==(numbers[i]+numbers[j]):
            return [i+1,j+1]
        elif target<(numbers[i]+numbers[j]):
            j-=1
        else:
            i+=1




print(pointer_approach(numbers,target))