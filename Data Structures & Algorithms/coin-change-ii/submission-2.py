class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, a):
            if a == amount:
                return 1          # one valid combination (empty pick)
            if i == len(coins):
                return 0          # no coins left
            if (i, a) in memo:
                return memo[(i, a)]
            if a > amount:
                return 0

            memo[(i,a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return memo[(i,a)]

        return dfs(0, 0)
