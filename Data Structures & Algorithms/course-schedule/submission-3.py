class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #the list is set up as a, b where you mmuch take course b first if you want to take course a

        adjlist = defaultdict(list)

        for course, prereq in prerequisites:
            adjlist[course].append(prereq)
        
        visit = set() #so we dont hit the same spot again
        cycle = set()

        def dfs(course):
            if course in visit:
                return True
            
            if course in cycle:
                return False  #cycle detected you won't be able to finish
            
            cycle.add(course)
            for pre in adjlist[course]:
                if not dfs(pre): #if we get a cycle
                    return False

            visit.add(course)
            cycle.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True