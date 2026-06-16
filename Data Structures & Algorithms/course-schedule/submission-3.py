        # graph = {i: [] for i in range(numCourses)}
        # for course, pre in prerequisites:
        #     graph[course].append(pre)

        # visiting = set()
        # visited = set()

        # def dfs(course):
        #     if course in visited:
        #         return True

        #     if course in visiting:
        #         return False

        #     visiting.add(course)
        #     for pre in graph[course]:
        #         if not dfs(pre):
        #             return False
        #     visiting.remove(course)
        #     visited.add(course)
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        
        # return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)

            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
                