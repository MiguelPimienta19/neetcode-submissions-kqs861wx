class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize pointers for buy (l) and sell (r), and max profit
        l, r = 0, 1
        maxP = 0

        # Iterate through prices
        while r < len(prices):
            if prices[l] < prices[r]:
                # Calculate profit and update max profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Update buy pointer if current price is lower
                l = r
            r += 1

        # Return the maximum profit
        return maxP
