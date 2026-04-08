class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:

            if heights[l] < heights[r]:

                curr_area = heights[l] * (r - l)
                area = max(area, curr_area)
                l += 1
            else:
                curr_area = heights[r] * (r - l)
                area = max(area, curr_area)
                r -= 1
        
        return area
