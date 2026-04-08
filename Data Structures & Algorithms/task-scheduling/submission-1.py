class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        maxheap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxheap)

        time = 0 
        q = deque() #holds [-cnt, idletime]

        while maxheap or q:
            time += 1

            if maxheap:
                cnt = 1 + heapq.heappop(maxheap) #add one because cnt is negative and to decrement add one
                if cnt: #if non zero
                    q.append([cnt, time + n]) #holds the cnt and when its available again
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time
