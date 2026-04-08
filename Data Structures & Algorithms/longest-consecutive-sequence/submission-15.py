class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #try set and n + 1 from what I could remember

        #I could sort but I don't want to do that needs to be O(n)

        #so I need to use a set of some what here and only loop through it once.
        if not nums:
            return 0

        ans = 1 

        num_set = set(nums)

        for n in nums:
            if n + 1 in num_set:
                length = 1
                while (length + n) in num_set:
                    length += 1
                    ans = max(length, ans)

        
        return ans
        