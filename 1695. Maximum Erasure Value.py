# You are given an array of positive integers nums and want to erase a subarray containing unique elements. 
# The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

# https://leetcode.com/problems/maximum-erasure-value/

nums = [5,2,1,2,5,2,1,2,5]


# a = set()
        
# sumset = []
# sum = 0
# pointer = 0
# if len(nums)!=1:
#     i = 0
#     while i<len(nums):
#         if nums[i] in a:
#             i = nums.index(nums[i],pointer,i)
#             sumset.append(sum)
#             i += 1
#             sum = nums[i]
#             a = set()
#             a.add(nums[i])
#             pointer = i
#             i+=1
#         else:
#             a.add(nums[i])
#             sum += nums[i]
#             i+=1
# else:
#     sum = nums[0]
# print(max(sum,max(sumset)))


seen=set() # track visited elements in the window
res=i=tot=0
for j in range(len(nums)):
    x=nums[j]                   # adjust the left bound of sliding window until you get all unique elements
    while i < j and x in seen: 
        seen.remove(nums[i])
        tot-=nums[i]
        i+=1                        
    tot+=x
    seen.add(x)
    res=max(res, tot)            
print(res)

# Took several help from the internet
