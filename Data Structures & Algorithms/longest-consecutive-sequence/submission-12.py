class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numset = set(nums) #cool thing is can search the whole thing at once

        longest = 1

        for n in nums:
            
            if (n + 1) in numset:
                length = 1
                while (n + length) in numset:
                    length += 1
                    longest = max(longest, length)
            
        return longest
