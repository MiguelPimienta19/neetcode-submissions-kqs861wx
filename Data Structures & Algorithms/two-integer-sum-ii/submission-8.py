class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            diff = target - numbers[i]

            while l <= r:
                m = (l + r) // 2

                if numbers[m] == diff:
                    return [i + 1, m + 1]
                
                elif numbers[m] > diff:
                    r = m - 1
                
                else:
                    l = m + 1
    
