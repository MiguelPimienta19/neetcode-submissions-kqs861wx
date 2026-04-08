
class Solution:
    def topKFrequent(self, nums, k):

        count = Counter(nums)


        frequency = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            frequency[freq].append(num)
        
        print(frequency)

        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for number in frequency[i]:
                if len(res) >= k:
                    return res
                res.append(number)
        
        return res
