class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        maping = { "}" : "{", "]": "[", ")": "("}

        for c in s:
            if c in maping:
                if stack and stack[-1] == maping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        