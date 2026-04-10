class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        repeat = set()
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in repeat:
                repeat.remove(s[l])
                l += 1
            repeat.add(s[r])
            count = max(count, r - l + 1 ) #because zero indexed...
        
        return count

            
        