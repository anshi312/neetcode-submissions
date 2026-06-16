class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        area = 0
        def dfs(r, c):
            nonlocal area
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            area += 1
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                dfs(r+dr, c+dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    maxArea = max(area, maxArea)
        return maxArea