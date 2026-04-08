class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # goal = len(nums) - 1

        # for i in range(len(nums) - 1, -1,-1):
        #     if i + nums[i] >= goal:
        #         goal = i #postion we are jumping from and change it 

        # return True if goal == 0 else False

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(nums) - 1:
                return True
            
            #if nums[i] == 0:
                #return False Don' think this is needed.
            
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)

