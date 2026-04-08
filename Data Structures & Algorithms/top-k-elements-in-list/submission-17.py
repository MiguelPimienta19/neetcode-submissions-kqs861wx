
class Solution:
    def topKFrequent(self, nums, k):

        counter = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)] #one thing could fill all spaces

        for key, value in counter.items():
            freq[value].append(key)
        

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) >= k:
                    return res
            
           

