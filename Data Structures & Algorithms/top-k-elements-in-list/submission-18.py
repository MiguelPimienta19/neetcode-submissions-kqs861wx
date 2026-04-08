
class Solution:
    def topKFrequent(self, nums, k):

        counter = Counter(nums)

        #now use a heap. 
        #remember I want to fill it with (i, num[i]) #where its sorted by freq

        heap = []

        for key, value in counter.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res


