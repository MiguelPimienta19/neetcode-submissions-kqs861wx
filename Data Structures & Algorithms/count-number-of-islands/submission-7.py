class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0 

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return #because we are out of bounds!!

            #but if not we continue to search and we make the postion 0
            grid[r][c] = "0"
            for dr, dc in directions:
                #why is it r + dr, c + dc??
                dfs(r + dr, c + dc)
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1 
        
        return count
        