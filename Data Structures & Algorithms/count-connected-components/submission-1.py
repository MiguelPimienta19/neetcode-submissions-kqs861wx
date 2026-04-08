class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        #question is really asking find the amount of connected graphs. 
        visit = set()
        def dfs(node):

            if node in visit:
                return True
            
            visit.add(node)
            for nei in adjList[node]:
                dfs(nei)
        
        res = 0
        for node in range(n): #run loop cuz graph is not connected.
            if node not in visit:
                dfs(node)
                res += 1 #we run dfs and find a connected graph. for every connected graph do res += 1
        return res
