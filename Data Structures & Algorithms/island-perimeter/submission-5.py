class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            if grid[new_r][new_c] == 1:
                                perimeter -= 1
        
        return perimeter
