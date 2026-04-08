class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROW, COL = len(board), len(board[0])

        #Okay this we are going to need to use dfs and also sets but then we should be able to pop
        #the set once we try a word and it dosent work
        #so this is a little bit of back tracking and also def also using sets lets tyr this 

        #we will also use an i to determine that we have reached the end of the word
        #and also see if we actually match the word too.
        word_set = set()
        def dfs(row, col, i):

            if i == len(word):
                return True
            
            if (row not in range(ROW) or col not in range(COL) or (row,col) in word_set or board[row][col] != word[i]):
                return False
            
            word_set.add((row,col))

            path = (dfs(row + 1, col , i + 1) or
            dfs(row - 1, col , i + 1) or
            dfs(row, col + 1 , i + 1) or
            dfs(row, col - 1 , i + 1))

            word_set.remove((row,col))

            return path 

        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False


        
        

