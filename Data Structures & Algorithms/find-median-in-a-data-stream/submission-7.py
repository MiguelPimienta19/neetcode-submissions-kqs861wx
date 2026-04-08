class MedianFinder:

    def __init__(self):
        #will be using two heaps small and large
        #large min heap
        #small max heap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        if self.large and num > self.large[0]: #this adds them to the heaps
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        

        #this fixes the balancing errors.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)
       
         

    def findMedian(self) -> float:

        #to get median we want to get max of small heap and min of large heap
        #then divide by two.
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0

    
