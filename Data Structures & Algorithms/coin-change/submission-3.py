class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}


        def dfs(i): 
            
            res = float("inf") #so we if we find a smaller value it changes

            if i in memo:
                return memo[i]

            if i == 0:
                return 0

            for coin in coins:
                if i - coin >= 0:
                    res = min(res, 1 + dfs(i - coin))
                        #for reference i will actually be amoun

            memo[i] = res
            return memo[i]


        return -1 if dfs(amount) >= float("inf") else dfs(amount) 


