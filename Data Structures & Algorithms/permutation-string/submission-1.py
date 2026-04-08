class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # 1) Build a frequency map for s1
        count1 = {}
        for c in s1:
            # for each character c in s1, increment its count in count1
            # count1.get(c, 0) returns the current count of c (or 0 if unseen)
            count1[c] = 1 + count1.get(c, 0)
        # ⇒ now count1 holds exactly how many of each letter s1 has

        # 2) How many distinct letters we need to match
        need = len(count1)
        # e.g. if s1 = "aabcbc", count1 = {'a':2,'b':2,'c':2}, then need = 3

        # 3) Try every possible starting position i in s2
        for i in range(len(s2)):
            # for each new start, reset our “window” counts & matched‐letter counter
            count2 = {}   # we’ll count letters in s2[i…j]
            curr   = 0    # how many distinct letters so far have exactly the right count

            # 4) Extend the window one char at a time, from j = i to end
            for j in range(i, len(s2)):
                # add s2[j] into our window‐frequency map
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                # 5) If we’ve added too many of s2[j] compared to what s1 needs, scrap this start
                if count2[s2[j]] > count1.get(s2[j], 0):
                    # e.g. s1 needs at most 2 'a's, but window now has 3 'a's → can’t ever match
                    break

                # 6) If this letter’s window‐count now exactly equals what s1 needs, we’ve “locked in” one distinct letter
                if count2[s2[j]] == count1.get(s2[j], 0):
                    curr += 1
                    # once per letter, when you hit its target frequency, you bump curr

                # 7) If we’ve now locked in all distinct letters, we found a permutation!
                if curr == need:
                    return True

        # 8) If no start i ever returned True, then there is no permutation
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

        