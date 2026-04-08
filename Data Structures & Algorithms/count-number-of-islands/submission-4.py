class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 4 possible directions to move (down, up, right, left)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]  
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 

        def bfs(r, c):

            q = deque()
            grid[r][c] = "0"  # mark the starting cell as visited (turn land into water)
            q.append([r, c])

            while q:
                row, col = q.popleft()  
                for dr, dc in directions: 
                    # Calculate neighbor position
                    nr, nc = row + dr, col + dc
                    
                    # Skip if out of bounds OR already water
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    
                    # Mark neighbor as visited and add to queue
                    grid[nr][nc] = "0"
                    q.append([nr, nc])
                    
        
        # Scan every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If we find land ("1"), run BFS to mark the whole island
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1  # increment island count
        
        return islands