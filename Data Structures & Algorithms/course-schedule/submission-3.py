class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited: 
                return False
            if pre_req[crs] == []:
                return True 

            visited.add(crs)
            for pre in pre_req[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_req[crs] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True