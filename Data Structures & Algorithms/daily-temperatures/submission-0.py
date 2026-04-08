class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #will contain the index and value


        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                 #while stack not empty and the temp we are at is greater than the last temp in stack
                 stackTemp, stackIndex = stack.pop()
                 res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return res

