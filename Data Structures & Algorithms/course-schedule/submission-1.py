"""

arra preq

preq[] = [a,b] indicated that uyou must b before taking a 

numCourses required to take labeled fro 0 to numCourses-1

return True if possible to take all and false if its impossible 

look for cycle: information if we visited this node already 

unvisited, visiting, visited (3 states) - DFS reaches a state twice 

build the graph from courses to its preq
dfs for each course
if dfs would find a course we visiting already - return False 
mark course when we visited it (if all prev preq are passed)

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites: 
            graph[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting: 
                return False 

            if course in visited: 
                return True 

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False 

            visiting.remove(course)

            visited.add(course)

            return True 

        for course in range(numCourses): 
            if not dfs(course):
                return False 

        return True 






        