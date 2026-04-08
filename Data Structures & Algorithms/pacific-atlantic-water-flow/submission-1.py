class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROW, COL = len(heights), len(heights[0]) 

        #need to find positions that can reach from pcf to atl. 
        #need to return a list of the ones that can do that
        pacific = set()
        atlantic = set()


        def dfs(row, col, ocean, prevheight):
            
            if (row < 0 or row >= ROW or col < 0 or col >= COL or heights[row][col] < prevheight or (row,col) in ocean):
                return 

            ocean.add((row, col))
            dfs(row + 1, col , ocean, heights[row][col]) 
            dfs(row - 1, col, ocean, heights[row][col]) 
            dfs(row, col + 1, ocean, heights[row][col]) 
            dfs(row, col - 1, ocean, heights[row][col])

        
        for row in range(ROW):
            dfs(row, 0, pacific, heights[row][0]) #this will get pacific side of row
            dfs(row ,COL - 1, atlantic, heights[row][COL - 1] ) #get atlantic side
        
        for col in range(COL):
            dfs(0, col, pacific, heights[0][col]) #atlantic side
            dfs(ROW - 1, col, atlantic, heights[ROW - 1][col]) #pacific side
        

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        



