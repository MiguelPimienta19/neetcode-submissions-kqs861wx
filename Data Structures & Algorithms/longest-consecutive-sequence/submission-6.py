class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        Numset = set(nums)
        print(Numset)

        longest = 1

        for n in nums:
            if (n + 1) in Numset:
                length = 1
                while (n + length) in Numset:
                    length += 1
                
                longest = max(longest, length)
        return longest