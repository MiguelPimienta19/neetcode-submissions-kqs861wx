class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # this is just here so we can check all four directions
        minutes = 0
        fresh = 0 


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        

        while q and fresh:
            for i in range(len(q)): #this loops through the levels
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            
            minutes += 1

        
        
        return minutes if fresh <= 0 else -1


        



















