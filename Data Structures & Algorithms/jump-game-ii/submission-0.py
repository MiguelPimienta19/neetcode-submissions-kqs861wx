class Solution:
    def jump(self, nums: List[int]) -> int:
        # memo = {}
        # def dfs(i):
        #     if len(nums) - 1 == i:
        #         return 0
        #     if i in memo:
        #         return memo[i]

        #     end = min(len(nums), i + nums[i] + 1)

        #     best = float("inf")
        #     for j in range(i + 1, end):
        #         best = min(best, 1 + dfs(j))   # one jump to j, then optimal from j

        #     memo[i] = best
        #     return best
        # return dfs(0)

        res = 0
        l, r = 0,0

        while r < len(nums) - 1:
            best = 0
            for i in range(l, r + 1):
                best = max(best, i + nums[i])
            l = r + 1
            r = best
            res += 1
        return res
