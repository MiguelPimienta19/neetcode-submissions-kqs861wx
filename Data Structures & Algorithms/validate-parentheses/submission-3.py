class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        maping = { "}" : "{", "]": "[", ")": "("}

        for c in s:
            if c in maping:
                if stack and stack[-1] == maping[c]: #make sure stack is not empty and that our last item is stack is the open version
                    stack.pop() # then pop it to maintain our valid solution
                else:
                    return False #if don't match and if stack is empty
            else:
                stack.append(c)
        
        if not stack: #stack has to be empty for final solution to be true
            return True
        else:
            return False
        