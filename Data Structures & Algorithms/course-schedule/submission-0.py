class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        preMap = {i : [] for i in range(numCourses)}
        #this builds our adj list.

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
       #visitset = all courses along the curent DFS path
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)
            return True


        #only need to run a for loop like these because graph may not be connected.
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

