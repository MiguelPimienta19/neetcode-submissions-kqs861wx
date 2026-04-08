class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1
        

        li = []

        for key,value in count.items():
            li.append((key,value))


        for i in range(len(li)):
            for j in range(i+1,len(li)):
                if li[i][1] < li[j][1]:
                    li[i],li[j] = li[j],li[i]
        res = []
        for i in range(k):
            res.append(li[i][0])
        return res
            

        


















