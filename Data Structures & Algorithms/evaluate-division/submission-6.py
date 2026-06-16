class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(a, b, product, visited):
            if a not in graph or b not in graph:
                return -1.0
            
            if a == b:
                return product

            visited.add(a)

            for nbh, val in graph[a]:
                if nbh not in visited:
                    result = dfs(nbh, b, product * val, visited)
                    if result != -1:
                        return result
            return -1.0

        result = []
        for a,b in queries:
            result.append(dfs(a,b,1,set()))

        return result