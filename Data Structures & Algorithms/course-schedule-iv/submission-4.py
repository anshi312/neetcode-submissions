# 0 -> 1
# 1 -> 2
# 2 -> 3

# course = 1
# query_pre = 0

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for prereq, course in prerequisites:
            graph[course].append(prereq)

        memo = {}

        def dfs(course, target, visited):
            if (course, target) in memo:
                return memo[(course, target)]

            if course == target:
                return True

            visited.add(course)

            for prereq in graph[course]:
                if prereq not in visited:
                    if dfs(prereq, target, visited):
                        memo[(course, target)] = True
                        return True

            memo[(course, target)] = False
            return False

        results = []
        for query_prereq, query_course in queries:
            result = dfs(query_course, query_prereq, set())
            results.append(result)

        return results
