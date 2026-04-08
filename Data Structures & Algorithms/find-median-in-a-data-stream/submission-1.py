class MedianFinder:

    def __init__(self):
        #two heaps, large, small, minheap, maxheap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num) #large heap will use min heap.
        else:
            heapq.heappush(self.small, -1 * num) #small heap will use max heap
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


         

    def findMedian(self) -> float:

        #to get median we want to get max of small heap and min of large heap
        #then divide by two.

        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0
