class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #this is pretty simple we just need to flatten it. 

        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, ROW * COL - 1

        while l <= r:

            m = (l + r)// 2

            i, j = m // COL, m % COL

            if target > matrix[i][j]:
                l = m + 1

            elif target < matrix[i][j]:
                r = m - 1
            
            else:
                return True
        
        return False