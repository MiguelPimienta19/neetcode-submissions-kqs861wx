class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0 #dont need to carry. 
            else:
                digits.append(1)
                one = 0 #dont need to carry any more
            i += 1
        digits.reverse()
        return digits

