from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2**31 - 1
        directions = [[1,0], [-1,0], [0,1], [0,-1]]  # use this to loop in the bfs

        # 0 is treasure chest
        # -1 water cell cannot be traversed
        # INF land cell that can be traversed.

        # we should run bfs from every land cell so we can update the rooms easily.
        def bfs(row, col):
            q = deque([(row, col)])         # queue holds (r, c)
            visited = set()                 # literally: visited = set()
            visited.add((row, col))
            steps = 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    # if we ever stand on a gate, steps is the distance
                    if grid[r][c] == 0:
                        return steps

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        # skip out-of-bounds, water, or already visited
                        if (
                            nr < 0 or nc < 0 or nr >= ROW or nc >= COL or
                            grid[nr][nc] == -1 or
                            (nr, nc) in visited
                        ):
                            continue

                        visited.add((nr, nc))
                        q.append((nr, nc))
                steps += 1

            return None  # no gate reachable

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
