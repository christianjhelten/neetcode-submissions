class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 

        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        done = set()

        def dfs(node):
            done.add(node)

            for neighbor in graph[node]:
                if neighbor in done: 
                    continue
                dfs(neighbor)
                
        dfs(0)

        return len(done) == n