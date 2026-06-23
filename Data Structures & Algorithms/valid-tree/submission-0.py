class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 

        graph = [[] for _ in range(n)]

        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        stack = [0]

        visited = set([0])


        while stack: 
            node = stack.pop()

            for nei in graph[node]:
                if nei not in visited: 
                    visited.add(nei)
                    stack.append(nei)

        return   len(visited) == n