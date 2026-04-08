class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowset = defaultdict(set)
        colset = defaultdict(set)
        square = defaultdict(set)

        #in sudoku we can only have unique elements in every row and column. 
        #each square must have values 1 - 9 as well. Or I guess can.

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rowset[row] or
                board[row][col] in colset[col] or
                board[row][col] in square[(row // 3, col // 3)] ):
                    return False

                rowset[row].add(board[row][col])
                colset[col].add(board[row][col])
                square[(row // 3, col // 3)].add(board[row][col])
        
        return True

                
