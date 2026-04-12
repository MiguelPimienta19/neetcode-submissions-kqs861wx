class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        level = [] #this is for each level to be appened into. 
        res = [] 
        def dfs(open_count, close_count):

            if open_count == close_count and open_count == n:
                res.append("".join(level))
                return

            if open_count < n:
                level.append("(")
                dfs(open_count + 1, close_count)
                level.pop()

            if close_count < open_count:
                level.append(")")
                dfs(open_count, close_count + 1)
                level.pop()
        dfs(0, 0)
        return res
