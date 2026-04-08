from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       

        heap = [] #max heap
        for x, y in points:
            distance = sqrt(x**2 + y**2) 

            heapq.heappush(heap, (-distance, (x, y)))
        
            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            distance, coord = heapq.heappop(heap)
            [res.append(coord)]

        return res



        
            
