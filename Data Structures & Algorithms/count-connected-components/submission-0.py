class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

            #this graph could be unconnected. but do I still need to worry about the prev here? 
            #but we don't need to watch for cycles we can just watch for visted egdes.
        visit = set()
        def dfs(node):

            if node in visit:
                return True
            
            visit.add(node)
            for nei in adjList[node]:
                dfs(nei)
        
        res = 0
        for connect in range(n):
            if connect not in visit:
                dfs(connect)
                res += 1
        return res
