class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        fresh = 0
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        ROW, COL = len(grid), len(grid[0])
        q = deque()

        #this grabs all of our rotten tomato postions.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        while q and fresh > 0:
            #SUPER IMPORTANT NEED TO DO ALL ADJACENT SIDES IN ONE MINUTE
            #GOT THAT WRONG. 
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1
        
        