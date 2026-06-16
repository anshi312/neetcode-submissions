class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # First row
        for c in range(1, n):
            if grid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]
        
        # First column
        for r in range(1, m):
            if grid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]
        
        # Rest of grid
        for r in range(1, m):
            for c in range(1, n):
                if grid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[m - 1][n - 1]