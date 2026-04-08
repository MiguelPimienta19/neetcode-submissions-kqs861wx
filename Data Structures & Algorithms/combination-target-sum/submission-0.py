class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        permutation = []

        def dfs(i, total):

            if total == target:
                res.append(permutation.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            permutation.append(nums[i])
            dfs(i, total + nums[i])
            
            permutation.pop()

            dfs(i + 1, total)
        dfs(0,0)
        return res

