class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == n-1 and y == n-1:
                return cost
            if visited[x][y]: continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    new_cost = max(cost, grid[nx][ny])
                    heapq.heappush(heap, (new_cost, nx, ny))

        