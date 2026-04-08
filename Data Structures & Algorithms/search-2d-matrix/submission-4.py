class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1 #search the rows for our target
        while top <= bottom: 
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]: #compare to mid row and last element in row
                top = mid_row + 1
            elif target < matrix[mid_row][0]: #compare to mid row and first element in row
                bottom = mid_row - 1
            else:
                break #we have found our target row now search for the specific value
            
    
        left_col, right_col = 0, n - 1
       # mid_row = (top + bottom) // 2 #have to set it again because it was in while loop before not global\

        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            if target > matrix[mid_row][mid_col]:
                left_col = mid_col + 1
            elif target < matrix[mid_row][mid_col]:
                right_col = mid_col - 1
            else:
                
                return True
        return False


