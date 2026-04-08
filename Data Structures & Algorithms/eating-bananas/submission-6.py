class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r #worst case we will be at r
        #and we will do a binary search to see which is the min that will hold satisfy conditions. 

        while l <= r:

            k = (l + r) // 2
            time = 0 

            #this sees if our choice of k acutally works
            for p in piles:
                time += math.ceil(float(p)/k) 

            if time <= h:
                res = k #res now becomes that k we gave.
                r = k - 1 #we are currently smaller let's eat less banannas.
            
            else:
                l = k + 1
                #time is too big lets start eating more banannas 
        return res


