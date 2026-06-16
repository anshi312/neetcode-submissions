class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            graph[pre].append(c)

        visiting = set()
        visited = set()
        result = []

        def dfs(course):
            if course in visiting: return []
            if course in visited: return True

            visiting.add(course)
            for n in graph[course]:
                if not dfs(n):
                    return False
            visiting.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c): return []
        
        return result[::-1]
