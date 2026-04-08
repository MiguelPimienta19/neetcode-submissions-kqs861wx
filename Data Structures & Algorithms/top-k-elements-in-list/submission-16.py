
class Solution:
    def topKFrequent(self, nums, k):

        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)] # we could have a number n amount of times


        for key, value in count.items():
            freq[value].append(key)

        res = []

        print(freq)

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
            
           

