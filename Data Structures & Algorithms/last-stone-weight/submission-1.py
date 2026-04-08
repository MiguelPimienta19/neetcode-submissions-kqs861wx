class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: #since we are doing negs we do > but it should be < 
                heapq.heappush(stones, first - second)
        if not stones:
            return 0

        return abs(stones[0])
