# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# https://leetcode.com/problems/reshape-the-matrix/

mat = [[1,2,3],[4,3,4]]
r = 1
c = 6

def reshape_matrix(mat,r,c):
    re_col = c
    if (len(mat)*len(mat[0])!=r*c):
        return mat
    else:
        reshaped_mat = []
        temp = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if c==1:
                    temp.append(mat[row][col])
                    reshaped_mat.append(temp)
                    temp = []
                    c = re_col
                else:
                    temp.append(mat[row][col])
                    c-=1
        return reshaped_mat
print(reshape_matrix(mat,r,c))

