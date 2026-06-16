class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph = {i: [] for i in range(numCourses)}
        # for c, pre in prerequisites:
        #     graph[pre].append(c)

        # visiting = set()
        # visited = set()
        # result = []

        # def dfs(course):
        #     if course in visiting: return []
        #     if course in visited: return True

        #     visiting.add(course)
        #     for n in graph[course]:
        #         if not dfs(n):
        #            return False
        #     visiting.remove(course)
        #     visited.add(course)
        #     result.append(course)
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c): return []
        
        # return result[::-1]



        #----------- topo sort ------------------#

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output[::-1]
