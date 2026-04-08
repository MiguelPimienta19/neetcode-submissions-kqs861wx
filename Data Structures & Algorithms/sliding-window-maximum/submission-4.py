class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        max_heap = []
        res = []
        for i in range(len(nums)):

            heapq.heappush(max_heap, (-nums[i], i))

            if i >= k - 1: #because we are 0 indexed. also we have reached window size
                            #also we dont use i + 1 it would go outta bounds

                while max_heap[0][1] <= i - k: #our max is outside of our window
                #needs this because i is where we are at and i - k would be the current window size. 
            
                    heapq.heappop(max_heap)
                
                res.append(-max_heap[0][0])
        
        return res
