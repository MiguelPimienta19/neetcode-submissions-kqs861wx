class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {i : [] for i in range(n + 1)}
        #given a undirected graph with no cycles find the cycle and return the edge that made it happen

        def dfs(node,parent):
            
            if node in cycle:
                return True
            
            cycle.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False #maybe switch this and line above 

        
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            cycle = set()

            if dfs(u, -1):
                return [u, v]
        return []