class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False

        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for ngh in graph[node]:
                if ngh == parent:
                    continue
                if ngh in visited:
                    return False
                if not dfs(ngh, node):
                    return False
            return True

        if not dfs(0, -1): return False
        return len(visited) == n