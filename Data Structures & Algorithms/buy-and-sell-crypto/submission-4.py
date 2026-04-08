class Solution:
   def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Pointer for the minimum price (buy day)
        res = 0  # Maximum profit

        for r in range(1, len(prices)):  # Iterate through possible sell days
            if prices[r] > prices[l]:
                # Calculate profit if selling on day `r`
                res = max(res, prices[r] - prices[l])
            else:
                # Update `l` to the current day if a lower price is found
                l = r

        return res

        