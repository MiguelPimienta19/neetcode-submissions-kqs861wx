class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return 
            #base case.

            #include
            subset.append(nums[i])
            dfs(i + 1)

            #this is when we pop and dont include after the base case. 
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res