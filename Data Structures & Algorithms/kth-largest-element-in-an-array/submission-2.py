class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums1 = [-i for i in nums]
        
        heapq.heapify(nums1)

        for _ in range(k - 1): 
            heapq.heappop(nums1)
        
        return -heapq.heappop(nums1)