class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers

        while l <= r:  # Continue until the pointers meet
            mid = (l + r) // 2  # Calculate the middle index

            if nums[mid] == target:  # Check if the middle element is the target
                return mid  
            elif nums[mid] < target:  
                l = mid + 1 
            else:  
                r = mid - 1  # Move the right pointer to the left of mid

        return -1 
