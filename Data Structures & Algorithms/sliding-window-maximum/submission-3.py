class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #this one is important!!

        #use a heap its most intuative. 

        #we use a heap but a max heap.

        #we keep adding to our heap till we read our length of k 

        #once we do that if our current max if smaller than our current window
        #change it.

        max_heap = []
        res = []
        for i in range(len(nums)):

            heapq.heappush(max_heap, (-nums[i], i)) #need the index of where we at too.

            if i >= k - 1: #because we are 0 indexed. also we have reached window size
                            #also we dont use i + 1 it would go outta bounds

                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                
                res.append(-max_heap[0][0])
        
        return res
