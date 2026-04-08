from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist = defaultdict(list)

        for course, pre in prerequisites:
            adjlist[course].append(pre)
 

        #we need to detrmine a cycle. maybe have two sets like a visted set and a cycle set??
        visit = set()
        cycle = set()

        def dfs(course):

            if course in visit:
                return True
            
            if course in cycle:
                return False

            # if adjlist[course] == []:
            #     return True
            
            cycle.add(course)
            for pre in adjlist[course]:
                if not dfs(pre):
                    return False
            
            visit.add(course)
            cycle.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



