class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        maping = { "}" : "{", "]": "[", ")": "("}

        for c in s:
            if c in maping:
                if stack and stack[-1] == maping[c]: #make sure stack is not empty and that our last item is stack is the open version
                    stack.pop()
                else:
                    return False #if don't match and if stack is empty
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        