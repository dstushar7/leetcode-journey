# Given a 2D matrix matrix, handle multiple queries of the following type:

#     Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:

#     NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#     int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2)

# Problem solved by prefix sum row and column


from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(ROW+1) for r in range(COL+1)] # List Comprehension

        # Prefix by columns
        for r in range(ROW):
            prefix = 0
            for c in range(COL):
                prefix += matrix[r][c]
                self.sumMat[r+1][c+1] = prefix

        # Prefix in rows
        for c in range(COL):
            prefix = 0
            for r in range(ROW):
                prefix += self.sumMat[r+1][c+1]
                self.sumMat[r+1][c+1] = prefix
        




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return (self.sumMat[row2][col2]-((self.sumMat[row2][col1-1]+self.sumMat[row1-1][col2])-self.sumMat[row1-1][col1-1]))