# You are given an integer array nums and an integer x. 
# In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
# Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/





nums = [1,1,4,2,3]
x = 5

def prefix_sum(nums):

    # prefix_sum(nums)[0] gives normal prefix sum
    # prefix_sum(nums)[1] gives the reverse prefix sum
    a = [sum(nums[ : i + 1]) for i in range(len(nums))]
    a_reverse = [sum(nums[i:len(nums)]) for i in range(len(nums))]
    dictionary = {i:a[i] for i in range(len(a))}
    reverse_dictionary = {i:a_reverse[i] for i in range(len(a))}
    return [dictionary,reverse_dictionary]

# Sliding Window
left = 0
right = len(nums)-1
operation = 0 
for i in range((len(nums)//2)+1):
    leftNum = nums[left]
    rightNum = nums[right]
    while x>=0:
        if x == 0:
            print(operation)
        else:
            pass

# Not completed



