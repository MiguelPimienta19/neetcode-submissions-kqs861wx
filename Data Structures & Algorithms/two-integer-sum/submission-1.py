class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            ans = target - nums[i]

            if ans in hash:
                return [hash[ans],i]

            hash[nums[i]] = i
        