# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

# https://leetcode.com/problems/search-a-2d-matrix/

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

col = len(matrix[0])

def binary_search(arr,high,low,target):
    if high<low:
        return False
    else:
        mid = (high+low)//2
        if arr[mid] == target:
            return True
        elif arr[mid]<target:
            return binary_search(arr,high,mid+1,target)
        else:
            return binary_search(arr,mid-1,low,target)



for row in matrix:
    if target<= row[col-1]:
        ans = binary_search(row,col-1,0,target)
        break
    else:
        ans = False
print(ans)