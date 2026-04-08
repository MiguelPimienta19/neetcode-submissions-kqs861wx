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


       
    # def isValidSudoku(self, board: List[List[str]]) -> bool:    
    #     cols = {}
    #     rows = {}
    #     grid = {}

    #     for row in range(len(board)):
    #         for col in range(len(board)):
    #             if board[row][col] == ".":
    #                 continue
                
    #             # Initialize row, column, and grid sets if not already done
    #             if row not in rows:
    #                 rows[row] = set()
    #             if col not in cols:
    #                 cols[col] = set()
    #             if (row // 3, col // 3) not in grid:
    #                 grid[(row // 3, col // 3)] = set()

    #             # Check for duplicates
    #             if (board[row][col] in rows[row] or
    #                 board[row][col] in cols[col] or
    #                 board[row][col] in grid[(row // 3, col // 3)]):
    #                 return False

    #             # Add the value to the corresponding row, column, and grid sets
    #             rows[row].add(board[row][col])
    #             cols[col].add(board[row][col])
    #             grid[(row // 3, col // 3)].add(board[row][col])

    #     return True

        