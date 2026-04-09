class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        bucket = [[] for i in range(len(nums) + 1)] #need the plus one because what if we have an element that fills up all list.
                                                    #pretty much just overflow
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0) 
        
        #puts it in our buckets. keeps everything O(n)
        for num, amount in freq.items():
            bucket[amount].append(num)
        
        #now loop backwards
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res