class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i : [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for nbh in graph[node]:
                if nbh == parent:
                    continue
                if nbh in visited:
                    return False
                if not dfs(nbh, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


        #################
        #   UNION FIND  #
        #################

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while parent[node] != node:
                parent[node] = find(parent[node])
                node = parent[node]
            return parent[node]

        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)

            if par1 == par2:
                return False

            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]

            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True




