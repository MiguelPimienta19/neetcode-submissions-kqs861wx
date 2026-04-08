class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1

        buckets = [[]for i in range(len(nums) +1 )]
        for key,value in count.items():
            buckets[value].append(key)

        print(buckets)

        ans = []
        for i in range(len(buckets) -1, 0, -1):
            for number in buckets[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans

