class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        path = set()
        #this will handle our paths
        #cuz it needs to be unique we can't hit the same area twice.


        def dfs(row, col, i): 
            if len(word) == i:
                return True
                #we managed to get our word. 

            #now handle out of bounds, if element of word not there, or if set in path. 
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or word[i] != board[row][col] or (row,col) in path):
                return False

            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or 
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
                )
                
            path.remove((row, col))
            #unmarks postions so other banches can use it. 
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col,0):
                    return True
        return False

