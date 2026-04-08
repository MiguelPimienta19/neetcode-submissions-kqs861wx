from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #okay I remember how to do this
        #my left pointer is the min amount of bannanas I can eat
        #my right is the max I can eat. 

        #I need my k to = the mid of that and find out how to do this 

        l = 1
        r = max(piles)
        res = float('inf')


        while l <= r:

            k = (l + r) // 2
            total = 0

            for banannas in piles:
                total += ceil(banannas/k)
           
            if total <= h:
                res = min(res, k)
                r = k - 1

            else:
                l = k + 1
        
        return res


