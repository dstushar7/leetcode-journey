# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# https://leetcode.com/problems/n-queens/

n = 4

# Creating the board 
board = [["."]*n for i in range(n)]
result = []
columns = set()
positive_diagonal = set() # r + c
negative_diagonal = set() # r - c


def backtrack(r):
    if(r==n):
        copy = ["".join(row) for row in board]
        result.append(copy)
        return
    for c in range(n):
        if c in columns or (r+c) in positive_diagonal or (r-c) in negative_diagonal:
            continue
        
        columns.add(c)
        positive_diagonal.add(r+c)
        negative_diagonal.add(r-c)
        board[r][c] = "Q"

        backtrack(r+1)

        columns.remove(c)
        positive_diagonal.remove(r+c)
        negative_diagonal.remove(r-c)
        board[r][c] = "."

backtrack(0)
print(result)

