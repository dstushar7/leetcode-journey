# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/


nums = [3,6,1,2,5]
k = 2

nums.sort()
count = 0 
length = len(nums)
slow,fast = 0,1
while(length>0):
    while(slow<len(nums) and fast<=len(nums)):
        if(fast==len(nums)):
            count+=1
            break
        else:
            slow_value = nums[slow]
            fast_value = nums[fast]
            if (fast_value-slow_value)<=k:
                fast += 1
            else:
                length -= fast
                slow = fast
                count += 1
    break

print(count)