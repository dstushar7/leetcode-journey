# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/search-insert-position/

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
        return start

nums = [1,3,5,6]
target = 7

index = binary_search(nums,0,len(nums)-1,target)

print(index)