class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #use xor because if we get two binary numbers the same we get 0
        #but if we get the single number it will be different then the rest.
        #bit number will be represented at the end. 

        res = 0
        for i in nums:
            res ^= i

        return res
        

