class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i : [] for i in range(numCourses)} 
        for course, pre in prerequisites:
            preMap[course].append(pre)
        #this builds an adj list for us. 


        output = []

        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False #cycle can't work
            if course in visit:
                return True #don't need to visit same node twice

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course) #remove it so when check new branch we don't have a false postive
            visit.add(course) #we checked entire branch already so don't need to see it again
            output.append(course) #add valid ordering
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output


            

            #this is topological sort!


