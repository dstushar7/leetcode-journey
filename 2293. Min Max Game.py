# https://leetcode.com/problems/min-max-game/


nums = [1,3,5,2,4,8,2,2]

n = len(nums)

def algorithm(n,arr):
    newNums = [0 for k in range(n//2)]
    if n==1:
        return arr
    else:
        for i in range(n//2):
            if (i%2)==0:
                newNums[i] = min(arr[2*i],arr[(2*i)+1])
            else:
                newNums[i] = max(arr[2*i],arr[(2*i)+1])
        length = len(newNums)
        return algorithm(length,newNums)

print(algorithm(n,nums))