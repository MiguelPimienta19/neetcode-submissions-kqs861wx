class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]   # initial fuel
        i = 0
        last = len(nums) - 1

        while jumps > 0:
            # spend one unit of fuel to move forward
            i += 1
            jumps -= 1

            if i >= last:
                return True

            # refuel if nums[i] gives more fuel than we have left
            jumps = max(jumps, nums[i])

        return i >= last
