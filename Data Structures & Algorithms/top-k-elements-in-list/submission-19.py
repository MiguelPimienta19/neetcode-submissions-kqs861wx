
class Solution:
    def topKFrequent(self, nums, k):

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #this puts the element in their frequency order now we need to make the list k length.
        for num, cnt in count.items():
            freq[cnt].append(num)

        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res