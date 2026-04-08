class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)
         
        for key,value in hash.items():
            if value == 1:
                return key