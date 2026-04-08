class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1) #since everything is based on s1
        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j],0) == count2[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force

        # s1 = sorted(s1)  # e.g. "ab" → ['a','b']

        # # outer loop over all start indices i
        # for i in range(len(s2)):  # i = 0,1,2,…

        #     # inner loop over all end indices j ≥ i
        #     for j in range(i, len(s2)):  # j = i,i+1,…,len(s2)-1
        #         # take the substring s2[i..j] (inclusive)
        #         substr = s2[i : j+1]
        #         # sort it so we can compare letter‐multisets
        #         substr = sorted(substr)

        #         # if this sorted substring matches sorted s1, we found a permutation
        #         if substr == s1:
        #             return True

        # # if we never returned True, no permutation of s1 is in s2
        # return False

        