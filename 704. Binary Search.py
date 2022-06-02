# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/binary-search/


def binary_search(arr,start,end,target):
    if start<=end:
        mid = (start+end)//2 # Flooring with this operator
        if arr[mid] == target :
            return mid
        elif arr[mid]>target:
            return binary_search(arr,start,mid-1,target)
        else:
            return binary_search(arr,mid+1,end,target)
    else:
        return -1

nums = [-1,0,3,5,9,12] 
target = 12



index = binary_search(nums,0,len(nums)-1,target)

print(index)


