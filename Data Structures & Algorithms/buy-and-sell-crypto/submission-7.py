class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1 
        return res 












#naive solution once I looked at it. It really is not that bad.
       # for i in range(len(prices)):
       #     buy = prices[i]
       #     for j in range(i +1, len(prices)):
       #         sell = prices[j] 
       #         res = max(res, sell - buy)
       # return res