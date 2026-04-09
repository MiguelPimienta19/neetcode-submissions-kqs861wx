class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        min_heap = []
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0) 
        
        #now that I have this set up I can make the heap.
        for num, amount in freq.items():

            heapq.heappush(min_heap, (amount, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
        

        