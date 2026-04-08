class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            #need this because we need to know which nodes both elements point to
            #it is undirected.
        
        cycle = set()
        def dfs(node, prev):

            if node in cycle:
                return False

            cycle.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0,-1) and n == len(cycle)


