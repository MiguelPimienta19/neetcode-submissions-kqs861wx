class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diction = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in diction:
                return [diction[diff], i]
            
            diction[nums[i]] = i 




