# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, 
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# https://leetcode.com/problems/triangle/

# Greedy Approach [Not Solved]
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# j = 0
# sum = 0 

# for row in triangle:
#     if len(row)==1:
#         sum += row[j]
#     else:
#         if row[j]>row[j+1]:
#             sum += row[j+1]
#             j += 1
#         else:
#             sum += row[j]
# print(sum)

# Dynamic Programming Recursion (TLE)
memo = [[-1] * len(triangle) for _ in range(len(triangle))]
def dfs(i, j):
    if i == len(triangle):
        return 0
    if memo[i][j] != -1:
        return memo[i][j]

    lower_left = triangle[i][j] + dfs(i + 1, j)
    lower_right = triangle[i][j] + dfs(i + 1, j + 1)
    memo[i][j] = min(lower_left, lower_right)
    return memo[i][j]

print(dfs(0,0))