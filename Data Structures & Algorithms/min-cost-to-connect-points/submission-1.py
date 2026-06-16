class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def manhattan(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return abs(x1 - x2) + abs(y1 - y2)

        in_mst = [False] * n

        min_heap = [(0, 0)]

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, curr = heapq.heappop(min_heap)

            if in_mst[curr]:
                continue

            in_mst[curr] = True
            mst_cost += cost
            edges_used += 1
            
            for next_point in range(n):
                if not in_mst[next_point]:
                    dist =  manhattan(curr, next_point)
                    heapq.heappush(min_heap, (dist, next_point))

        return mst_cost
