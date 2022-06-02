#https://leetcode.com/problems/running-sum-of-1d-array/

nums = [1,1,1,1,1]

sum = 0 

sum_list = []

for i in nums:
    sum = sum+i
    sum_list.append(sum)

print(sum_list)
