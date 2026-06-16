# 0 -> 1
# 1 -> 2
# 2 -> 3

# course = 1
# query_pre = 0

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for prereq, course in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        prereq_sets = [set() for _ in range(numCourses)]

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            prereq = queue.popleft()

            for course in graph[prereq]:
                prereq_sets[course].add(prereq)
                prereq_sets[course].update(prereq_sets[prereq])
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        result = []
        for u, v in queries:
            result.append(u in prereq_sets[v])

        return result





        # graph = defaultdict(list)

        # for prereq, course in prerequisites:
        #     graph[course].append(prereq)

        # memo = {}

        # def dfs(course, target, visited):
        #     if (course, target) in memo:
        #         return memo[(course, target)]

        #     if course == target:
        #         return True

        #     visited.add(course)

        #     for prereq in graph[course]:
        #         if prereq not in visited:
        #             if dfs(prereq, target, visited):
        #                 memo[(course, target)] = True
        #                 return True

        #     memo[(course, target)] = False
        #     return False

        # results = []
        # for query_prereq, query_course in queries:
        #     result = dfs(query_course, query_prereq, set())
        #     results.append(result)

        # return results
