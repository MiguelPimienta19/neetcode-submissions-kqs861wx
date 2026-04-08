from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #make a heap out of this it is easy.

        #given 2d array where points[i] = [xi, yi] rep cooridents.

       # return k closes points to origin (0,0)

        #use a heap but transform the distance.


        #use a max heap because we want the smallest (closest) points

        #in heap we could hold the distance and the tupal for distance.

        heap = [] #max heap
        for x, y in points:
            distance = sqrt(x**2 + y**2) 

            heapq.heappush(heap, (-distance, (x, y)))
        
            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            [res.append(heapq.heappop(heap)[1])]
            
        return res



        
            
