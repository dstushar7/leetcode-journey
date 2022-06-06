# You are given a 0-indexed array nums that consists of n distinct positive integers. 
# Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].

# It is guaranteed that in the ith operation:

#     operations[i][0] exists in nums.
#     operations[i][1] does not exist in nums.

# Return the array obtained after applying all the operations.

# https://leetcode.com/problems/replace-elements-in-an-array/

nums = [1,2]
operations = [[1,3],[2,1],[3,2]]
nums_map = {k: v for v, k in enumerate(nums)}


for i in operations:
    if i[0] in nums_map:
        temp_index = nums_map[i[0]]
        del nums_map[i[0]]
        nums_map[i[1]] = temp_index
        nums[temp_index] = i[1]

print(nums)
    
