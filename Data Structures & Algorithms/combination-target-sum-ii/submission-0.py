class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combinations = []

        def dfs(i, total):
            if target == total:
                res.append(combinations.copy())
                return
            if total > target or i == len(candidates):
                return
            
            combinations.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            combinations.pop()
            
            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j, total)
        
        dfs(0,0)
        return res