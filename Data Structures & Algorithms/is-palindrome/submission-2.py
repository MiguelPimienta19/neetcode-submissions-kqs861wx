class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftp , rightp = 0, len(s) - 1

        while leftp < rightp:

            while leftp < rightp and not self.isalphnum(s[leftp]):
                leftp += 1
            while leftp < rightp and not self.isalphnum(s[rightp]):
                rightp -= 1
            
            if s[leftp].lower() != s[rightp].lower():
                return False
            leftp, rightp = leftp+1,rightp-1
        return True






    def isalphnum(self, c):
        return ((ord("A") <= ord(c) <= ord("Z")) or
        (ord("a") <= ord(c) <= ord("z")) or
        (ord("0") <= ord(c) <= ord("9")))
        
        
        
        
        
        
        
        
        
        
        
        
        
        # newStr = ''
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
        