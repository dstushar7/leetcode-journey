# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# https://leetcode.com/problems/pascals-triangle/

numRows = 5

def pascal_triangle(numRows):
    triangle = []
    for i in range(numRows):
        temp = []
        for j in range(i+1):
            if(i>0) and (j>0) and (j<i):
                temp.append(triangle[i-1][j]+triangle[i-1][j-1])
            else:
                temp.append(1)
        triangle.append(temp)
    return triangle

print(pascal_triangle(5))
