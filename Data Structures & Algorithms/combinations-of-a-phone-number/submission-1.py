class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        res = []
        path = [] #this will go back tracking. 

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


        def dfs(i): #this should be the index and 

            if i == len(digits):
                res.append("".join(path)) #I think this just makes it a string and I can append that to our res
                return
            

            for c in digitTochar[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop() #this it try a different letter.
            
        

        dfs(0)
        return res

