class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            #odd length
            l,r = i,i #aba
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1


            #even length
            l,r = i, i + 1 #abba 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l-=1
                r+=1
        return res

        # for i in range(len(s)):
        #     for offset in [0,1]:
        #         l, r = i, i + offset
        #         while l >= 0 and r < len(s) and s[l] == s[r]:
        #             if (r - l + 1) > reslen:
        #                 res = s[l:r+1]
        #                 reslen = r - l + 1
        #             l -= 1
        #             r += 1
        # return res