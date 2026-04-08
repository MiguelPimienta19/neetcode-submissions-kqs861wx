class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsets = []

        def dfs(i): 
            if len(nums) == i:
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()

            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j +=1
            dfs(j)
        
        dfs(0)
        return res