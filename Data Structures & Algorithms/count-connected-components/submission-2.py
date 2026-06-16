class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)

                for nbh in graph[curr]:
                    if nbh not in visited:
                        stack.append(nbh)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components