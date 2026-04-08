class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        cols = defaultdict(set)
        rows = defaultdict(set)
        grid = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in grid[(row//3,col//3)]):
                    return False

                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                grid[(row//3,col//3)].add(board[row][col])
        return True
        