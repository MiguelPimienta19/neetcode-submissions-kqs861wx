class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []


        def dfs(i): 

            if i == len(nums):
                res.append(subset.copy())
                return #for the call stack 
            
            subset.append(nums[i])
            dfs(i + 1) #dive deeper into the list.
            subset.pop() #now when we backtrack exlude a number
            dfs(i + 1)
        
        dfs(0)
        return res

