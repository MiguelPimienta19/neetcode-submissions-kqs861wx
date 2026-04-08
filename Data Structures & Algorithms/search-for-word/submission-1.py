class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        
        seen = set() #so we don't have to hit the same word twice

        def dfs(row, col, i):

            if i == len(word):
                return True
            
            if (row not in range(ROWS) or col not in range(COLS) or word[i] != board[row][col] or (row, col) in seen):
                return False

            seen.add((row,col))

            route = (dfs(row + 1, col, i + 1) or 
                    dfs(row - 1, col, i + 1) or 
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1))
            
            seen.remove((row,col))
            return route
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False

