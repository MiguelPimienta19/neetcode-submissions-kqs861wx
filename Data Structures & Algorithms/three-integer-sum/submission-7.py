class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #do not contain any duplicates.

        nums.sort()
        dup = set() #this will maintain all duplicate entrys

        for i in range(len(nums)):

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                
                else:
                    dup.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return [list(trip) for trip in dup]
