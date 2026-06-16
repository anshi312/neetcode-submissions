class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # graph = {i:[] for i in range(n)}
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # visited = set()
        # components = 0

        # def dfs(node):
        #     stack = [node]
        #     while stack:
        #         curr = stack.pop()
        #         if curr in visited:
        #             continue
        #         visited.add(curr)

        #         for nbh in graph[curr]:
        #             if nbh not in visited:
        #                 stack.append(nbh)

        # for node in range(n):
        #     if node not in visited:
        #         components += 1
        #         dfs(node)
        # return components

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p1] = p2
                rank[p1] += rank[p2]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)

        return result
