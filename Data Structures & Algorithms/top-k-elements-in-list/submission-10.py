class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        
        minheap = []
        for num in count.keys():
            heapq.heappush(minheap, (count[num], num)) # we order heap by counter values.
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for i in range(k):
           res.append(heapq.heappop(minheap)[1])
        return res 







        





