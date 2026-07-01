"""Determine if a 9 x 9 Sudoku board is valid. """

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box = [set() for _ in range(9)] # create 9 different sets denoting each box

        # check row-wise
        for i in range(9):

            row_set = set()
            col_set = set()
            
            # scan row by row, notice how i,j are flipped in this and the one col_items
            for j in range(9):
                # for row
                row_item = board[i][j]
                if row_item != ".":
                    if row_item in row_set:
                        return False
                    row_set.add(row_item)
                
                # for col
                col_item = board[j][i]
                if col_item != ".":
                    if col_item in col_set:
                        return False
                    col_set.add(col_item)
                
                # for box
                if board[i][j] != ".":
                    box_id = (i // 3) * 3 + (j // 3) # i responsible to push box number by 3

                    if board[i][j] in box[box_id]:
                        return False
                    box[box_id].add(board[i][j])

        return True