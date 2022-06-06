# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.


# https://leetcode.com/problems/valid-sudoku/


from typing import Counter

from numpy import square


board = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

def check_board_validity(board):

    def check(board):
        for row in board:
            dictionary = Counter(row)
            if dictionary["."]:
                del dictionary['.']
            for i in dictionary.values():
                if i>1:
                    return False
        return True

    def transpose_matrix(matrix):
        transpose_matrix = []
        temp_matrix = []

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                temp_matrix.append(matrix[j][i])
            transpose_matrix.append(temp_matrix)
            temp_matrix=[]
        return transpose_matrix


    # Row Check
    if (check(board)==False):
        return False

    # Column Check
    column = transpose_matrix(board)
    if (check(column)==False):
        return False
    
    # Square check
    square_cut = []
    for i in range(3):
        for j in range(3):
            temp = []
            for row in range(3*i,3*(i+1)):
                for col in range(3*j,3*(j+1)):
                    temp.append(board[row][col])
            square_cut.append(temp)
            if(check(square_cut)==False):
                return False
            square_cut = []

    return True

print(check_board_validity(board))

# Hardest that I solved alone :3