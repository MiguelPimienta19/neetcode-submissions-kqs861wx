class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)

        res = 0
        for i in nums:
            if count[i] == 1:
                return i