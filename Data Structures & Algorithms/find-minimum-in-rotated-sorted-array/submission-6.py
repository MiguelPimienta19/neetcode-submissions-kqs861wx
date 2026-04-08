class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If not rotated (or single element), first is min
        if nums[0] <= nums[-1]:
            return nums[0]

        lo, hi = 0, len(nums) - 1
        # Binary‑search for pivot (smallest element)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                # pivot is to the right of mid
                lo = mid + 1
            else:
                # pivot is at mid or to its left
                hi = mid
        # lo == hi == index of minimum
        return nums[lo]
