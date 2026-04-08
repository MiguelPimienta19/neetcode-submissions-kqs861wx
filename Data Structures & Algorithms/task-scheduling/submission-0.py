class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        Max_heap = [-task for task in count.values()]
        heapq.heapify(Max_heap)

        time = 0 
        q = deque() #pairs [-count, idleTime] 

        while Max_heap or q:
            time += 1

            if Max_heap:
                cnt = 1 + heapq.heappop(Max_heap) #we can add one cuz its negative
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(Max_heap, q.popleft()[0])
            
        return time 


