class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []

        digitTochar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        path = []
        def dfs(idx: int):
            if idx == len(digits):
                res.append("".join(path))
                return
            for ch in digitTochar[digits[idx]]:
                path.append(ch)
                dfs(idx + 1)
                path.pop()

        dfs(0)
        return res

