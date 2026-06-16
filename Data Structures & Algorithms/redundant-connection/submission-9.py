class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(num):
            result = num
            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(num1, num2):
            par1 = find(num1)
            par2 = find(num2)

            if par1 == par2:
                return False

            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]

            return True

        for num1, num2 in edges:
            if not union(num1, num2):
                return [num1, num2]
                