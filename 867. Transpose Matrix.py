# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# https://leetcode.com/problems/transpose-matrix/




matrix = [[1,2,3],[4,5,6],[7,8,9]]

transpose_matrix = []
temp_matrix = []

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        temp_matrix.append(matrix[j][i])
    transpose_matrix.append(temp_matrix)
    temp_matrix=[]
    
print(transpose_matrix)