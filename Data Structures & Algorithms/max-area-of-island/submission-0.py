class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROW, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            nonlocal area

            if r < 0 or c < 0 or r >= ROW or c >= COLS or grid[r][c] == 0:
                return
            
            area += 1
            grid[r][c] = 0 #so we don't hit the same area twice. 

            dfs(r + 1 , c)
            dfs(r - 1, c)
            dfs(r , c + 1)
            dfs(r, c - 1)

        
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 0 
                    dfs(r,c)
                    maxArea = max(area, maxArea)

        return maxArea