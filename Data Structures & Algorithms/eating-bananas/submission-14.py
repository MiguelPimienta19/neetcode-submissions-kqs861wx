


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            hour_spent = 0 #this is what is gonna give us our answer



            for pile in piles:
                hour_spent += math.ceil(pile /m)

            if hour_spent <= h:
                r = m - 1
                res = m
            else:
                l = m + 1 
                
        return res