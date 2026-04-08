class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1

        buckets = [[]for i in range(len(nums)+1)]
        for key,value in count.items():
            buckets[value].append(key)

        
        ans = []

        for i in range(len(buckets) -1, 0, -1):
            for number in buckets[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans

        






















# # simpler way but O(M + K) time
#         count = {}
#         for i in nums:
#             if i not in count:
#                 count[i] = 0
#             count[i] +=1

#         #Create a singular list containing all (number, frequency) pairs
#         li = []
#         for key,value in count.items():
#             li.append((key,value))

#         # Step 3: Sort the singular list based on the frequency
#         for i in range(len(li)):
#             for j in range(i+1,len(li)):
#                 if li[i][1] < li[j][1]:
#                     li[i],li[j] = li[j],li[i]
        
#         # Step 4: Extract the top k numbers from the sorted list
#         res = []
#         for i in range(k):
#             res.append(li[i][0])     #Append the number, not the frequency
#         return res
            

        


















