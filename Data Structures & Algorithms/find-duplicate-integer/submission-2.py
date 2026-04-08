class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()

        for i in range(len(nums)):
            if nums[i] in numset:
                return nums[i]
            numset.add(nums[i])
