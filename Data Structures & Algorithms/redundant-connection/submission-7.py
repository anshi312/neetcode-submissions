class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)
        
        # def find(x):
        #     if x != parent[x]:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: return False

            elif rank[rootA] > rank[rootB]:
                parent[rootB] = parent[rootA]
            elif rank[rootB] > rank[rootA]:
                parent[rootA] = parent[rootB]
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True

        for u,v in edges:
            if not union(u,v):
                return[u,v]