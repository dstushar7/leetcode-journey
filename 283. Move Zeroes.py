# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# https://leetcode.com/problems/move-zeroes/




nums = [0,1,0,3,12]

i=0
length = len(nums)
while i<length:
    if nums[i] == 0:
        nums.pop(i)
        nums.append(0)
        length-=1
    else:
        i+=1
print(nums)