class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #--------------#
        #  brute force #
        #--------------#

        # if n == 1:
        #     return [0]

        # graph = defaultdict(list)
        # for a, b in edges:
        #     graph[a].append(b)
        #     graph[b]. append(a)

        # def dfs(node, parent):
        #     max_depth = 0
        #     for nbh in graph[node]:
        #         if nbh != parent:
        #             depth = 1 + dfs(nbh, node)
        #             max_depth = max(max_depth, depth)
        #     return max_depth

        # min_height = float('inf')
        # result = []

        # for i in range(n):
        #     height = dfs(i, -1)

        #     if height < min_height:
        #         min_height = height
        #         result = [i]
        #     elif height == min_height:
        #         result.append(i)

        # return result

        #--------------#
        #like topo sort# 
        #--------------#

        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            degree[a] += 1
            graph[b].append(a)
            degree[b] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            leaves_count = len(queue)
            remaining -= leaves_count

            for _ in range(leaves_count):
                leaf = queue.popleft()

                for nbh in graph[leaf]:
                    degree[nbh] -= 1
                    if degree[nbh] == 1:
                        queue.append(nbh)

        return list(queue)

